import click
import pickle
import os
from utility import load_objects
from html_to_recipe import html_to_recipe
from meal_planner import MealPlanner

@click.group
def cli():
    pass

@click.command
@click.option('-w', '--webpage', prompt="Enter a URL")
def createmeal(webpage):    
    if webpage == None:
        return
    recipe = html_to_recipe(webpage)
    filename = 'recipe.pkl'  
    
    with open(filename, 'ab') as f:
        pickle.dump(recipe, f, pickle.HIGHEST_PROTOCOL)
    

@click.command
def listmeals():  

    if not os.path.exists('recipe.pkl'):
        click.echo("No file could be found, try adding new recipe to create file")
        return
    recipes = load_objects('recipe.pkl')
    
    if len(recipes) == 0:
        click.echo("No recipes could be found")
    for r in recipes:
        click.echo(r.name)

@click.command
def createmealplan():
    mealplan = MealPlanner()
    mealplan.generate_meal_plan()
    mealplan.print_meal_plan()

cli.add_command(createmeal)
cli.add_command(listmeals)
cli.add_command(createmealplan)

if __name__ == '__main__':
    cli()