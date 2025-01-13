import click
import datetime
from html_to_recipe import html_to_recipe
from utility import save_object, load_objects
from meal_planner import MealPlanner

def main_menu():
    day = datetime.datetime.today().weekday()

    while True:
        prompt = click.prompt("""
Meal planner:
                              
1. Pull recipe from webpage
2. Print all recipes
3. Print meal plan
q. Quit
""")
        
        match prompt:
            case '1':
                recipes = load_objects('test_recipe.pkl')
                webpage = click.prompt("Enter a recipe webpage")
                recipe = html_to_recipe(webpage)
                print(f"{recipe.name} has been loaded")
                if recipe not in recipes:
                    recipes.append(recipe)
                save_object(recipes, 'test_recipe.pkl')
            case '2':
                if len(recipes) == 0:
                    recipes = load_objects('test_recipe.pkl')
                for r in recipes:
                    print(r.name)

            case '3':
                meal_plan = MealPlanner()
                meal_plan.generate_meal_plan()
                meal_plan.print_meal_plan()

                print(f"\nTodays meal is {meal_plan.meal_plan[day].name}")
            case 'q':
                return