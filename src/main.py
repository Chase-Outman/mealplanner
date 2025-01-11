
from recipe import Recipe, Ingredient, UnitType
from html_to_recipe import html_to_recipe, get_ingredient_data
from utility import save_object, load_objects

def main():
    # recipe with multiple ingredient lists https://www.allrecipes.com/greek-beef-stuffed-onions-salantourmasi-recipe-8699944
            
    #TODO get secondary ingredient list within orginal list
    #soup1 = BeautifulSoup(r.text, 'html.parser').find_all('p', 'mm-recipes-structured-ingredients__list-heading text-title-200')
    
    recipe1 = html_to_recipe("https://www.allrecipes.com/greek-beef-stuffed-onions-salantourmasi-recipe-8699944")
    recipe2 = html_to_recipe("https://www.allrecipes.com/recipe/275590/marry-me-chicken/")
    recipe3 = html_to_recipe("https://www.allrecipes.com/bang-bang-chicken-nuggets-recipe-8767654")
    recipe4 = html_to_recipe("https://www.allrecipes.com/za-atar-chicken-wings-recipe-8754648")

    recipes = [recipe1, recipe2, recipe3, recipe4]

    #save_object(recipes, 'test_recipe.pkl')

    loaded_recipes = load_objects('test_recipe.pkl')
    for recipe in loaded_recipes:
        print(recipe.name)


if __name__ == "__main__":
    main()