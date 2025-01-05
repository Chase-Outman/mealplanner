import requests

from recipe import Recipe, Ingredient, UnitType
from html_to_recipe import html_to_ingredient_list

def main():
    test = html_to_ingredient_list("https://www.allrecipes.com/hotdog-roll-ups-recipe-8678872")
    for i in test:
        print(i)


if __name__ == "__main__":
    main()