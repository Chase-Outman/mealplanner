import requests
import re
import json
from bs4 import BeautifulSoup

from recipe import Recipe, Ingredient, UnitType
from html_to_recipe import html_to_recipe, get_ingredient_data

def main():
    # recipe with multiple ingredient lists https://www.allrecipes.com/greek-beef-stuffed-onions-salantourmasi-recipe-8699944

    recipe = html_to_recipe("https://www.allrecipes.com/recipe/228823/quick-beef-stir-fry/")

    recipe.print_recipe()

    # r = requests.get("https://www.allrecipes.com/ploughman-s-sandwich-recipe-8737059")

    # soup = BeautifulSoup(r.text, 'html.parser').find_all('ul', 'mm-recipes-structured-ingredients__list')
    
    # # for s in soup:
    # #     for a in s.find_all('p'):
    # #         print(a.find_all(attrs = {"data-ingredient-quantity":"true"}))

    # #print(soup[0].find_all(attrs = {"data-ingredient-quantity":"true"}))
    # #print(soup[0].find_all('p'))     

    # get_ingredient_data(soup)
                
            
    #TODO get secondary ingredient list within orginal list
    #soup1 = BeautifulSoup(r.text, 'html.parser').find_all('p', 'mm-recipes-structured-ingredients__list-heading text-title-200')
    
   

    

    
    # list_obj = soup.findAll('ul')
    
    # for l in list_obj:
    #     print(f"\n{l}")
    

if __name__ == "__main__":
    main()