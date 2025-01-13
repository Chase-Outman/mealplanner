import click
from recipe import Recipe, Ingredient, UnitType
from html_to_recipe import html_to_recipe, get_ingredient_data
from utility import save_object, load_objects
from user_interface import main_menu

def main():
    # recipe with multiple ingredient lists https://www.allrecipes.com/greek-beef-stuffed-onions-salantourmasi-recipe-8699944
            
    #TODO get secondary ingredient list within orginal list
    #soup1 = BeautifulSoup(r.text, 'html.parser').find_all('p', 'mm-recipes-structured-ingredients__list-heading text-title-200')
    
    main_menu()


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")
if __name__ == "__main__":
    main()