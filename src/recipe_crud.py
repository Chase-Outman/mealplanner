import click
import utility
from html_to_recipe import html_to_recipe


@click.command()
@click.option('-w', '--webpage', prompt="Enter a URL")
@click.pass_context
def add(ctx: click.Context, webpage):
    recipe = html_to_recipe(webpage)
    filename = 'recipe.pkl'     
    utility.save_object(recipe, filename)
    ctx.obj["recipes"].append(recipe)
    

@click.command()
@click.pass_context
def list(ctx: click.Context):
    recipes = ctx.obj["recipes"]
    
    if len(recipes) == 0:
        click.echo("No recipes could be found")
    for i, r in enumerate(recipes):
        click.echo(f"{i}-{r.name}")

@click.command()
@click.argument("index", type=int, required=1)
@click.pass_context
def delete(ctx:click.Context, index):
    recipes = ctx.obj["recipes"]
    recipes.pop(index)
    
    #erases everthing on file
    open('recipe.pkl', 'w').close()

    for r in recipes:
        utility.save_object(r,'recipe.pkl')
