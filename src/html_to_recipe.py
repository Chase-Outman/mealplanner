import requests
import re
from bs4 import BeautifulSoup
import json
from recipe import *


def html_to_recipe(webpage):
    pattern = r"^https://www.allrecipes.com/"
    if not re.search(pattern, webpage):
        print("Not an all recipes recipe")
        return
    request = requests.get(webpage)

    html = BeautifulSoup(request.text, 'html.parser')

    #find the script tag that holds the recipe information
    recipe_script = html.find(id = "allrecipes-schema_1-0").get_text()

    #removed starting and ending square brackets to convert to json format
    recipe_script = recipe_script.removeprefix('[').removesuffix(']').strip()
    data = json.loads(recipe_script)

    ingredient_list = html.find_all('ul', 'mm-recipes-structured-ingredients__list')

    
    #get recipe name from html title
    recipe_name = html.title.text
    ingredients = get_ingredient_data(ingredient_list)
    instructions = []
    for d in data["recipeInstructions"]:
        instructions.append(d['text'])

    return Recipe(recipe_name, ingredients, instructions)

def get_ingredient_data(ingredient_list):
    ingredients = []
    for list in ingredient_list:
        for item in list.find_all('p'):
            
            quantity_data = item.find_all(attrs = {"data-ingredient-quantity":"true"})
            unit_type_data = item.find_all(attrs = {"data-ingredient-unit":"true"})
            name_data = item.find_all(attrs = {"data-ingredient-name":"true"})

            quantity = None
            unit_type = None
            name = name_data[0].text

            if len(quantity_data) != 0:
                quantity = quantity_data[0].text
            if len(unit_type_data) != 0:
                unit_type = unit_type_data[0].text
            
            ingredients.append(Ingredient(name, item.text,  quantity, unit_type))

    return ingredients

 
