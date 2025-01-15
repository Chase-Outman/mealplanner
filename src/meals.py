import click
import recipe_crud
import os
from utility import load_objects

@click.group
@click.pass_context
def cli(ctx: click.Context):
    if not os.path.exists('recipe.pkl'):
        open('recipe.pkl', 'w').close()
    recipes = load_objects('recipe.pkl')
    ctx.obj = {"recipes": recipes}

@cli.group
def recipe():
    pass


recipe.add_command(recipe_crud.add)
recipe.add_command(recipe_crud.list)
recipe.add_command(recipe_crud.delete)


if __name__ == "__main__":
    cli()