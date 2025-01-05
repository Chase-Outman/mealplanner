import requests
from recipe import *

def html_to_ingredient_list(web_address):
    r = requests.get(web_address)
    lines = r.text.split('\n')
    start = 0
    end = 0


    for line in lines:
        if "recipeIngredient" in line:
            start = lines.index(line)
        if "recipeInstructions" in line:
            end = lines.index(line)

    raw_ingredients = lines[start+1:end]
    cleaned_ingredients = []
    for i in raw_ingredients:
        cleaned = i.replace("\"", "").replace(",", "").replace(u"\xa0", " ")
        if '[' not in cleaned:
            cleaned = cleaned.replace(']', "")

        cleaned_ingredients.append(cleaned)

    ingredients = []
    for i in cleaned_ingredients:
        s = i.split(" ")
        amount = __get_ingredient_amount(s[0])
        unit_type = __get_unit_type(s[1])
        name = i.replace(s[0], "").replace(s[1], "")  
        
        ingredient = Ingredient(__get_cleaned_name(name).strip(), amount, unit_type)
        ingredients.append(ingredient)

    return ingredients

    
        
def __get_cleaned_name(name):
    if '(' in name:        
        return name.replace(name[name.index('(')-1:name.index(')')+1], "")
    return name
    

def __get_ingredient_amount(amount):
    if "/" in amount:
        upper_lower = amount.split("/")
        return (float)(upper_lower[0]) / (float)(upper_lower[1])
    return amount

def __get_unit_type(unit_type):
    if "Tbsp" in unit_type:
        return UnitType.TABLESPOON
    if "tsp" in unit_type:
        return UnitType.TEASPOON
    if "cup" in unit_type:
        return UnitType.CUPS
    return UnitType.UNIT    


    