from enum import Enum

class Recipe():
    def __init__(self, name, ingredients, intructions = None):
        self.name = name
        self.ingredients = ingredients
        self.intructions = intructions

    def __str__(self):
        return f"{self.name}\n\n{'\n'.join(str(ingredient) for ingredient in self.ingredients)}\n\n{'\n'.join(self.intructions)}"
    
    def __eq__(self, value):
        return self.name == value.name
    
    def print_recipe(self):
        print(f"{self.name}")
        print(f"\n{'\n'.join(str(ingredient) for ingredient in self.ingredients)}\n")

        for i in range(len(self.intructions)):
            print(f"Step {i+1}")
            print(f"\t{self.intructions[i]}\n")


        
class UnitType(Enum):
    CUPS='cups'
    TEASPOON = 'teaspoon'
    TABLESPOON = 'tablespoon'
    POUND = 'pound'
    UNIT = ''
    

class Ingredient():
    def __init__(self, name, ingredient_text, units=None, unit_type=None):
        self.name = name
        self.ingredient_text = ingredient_text
        self.units = units
        self.unit_type = unit_type
    
    def __str__(self):
        return  self.ingredient_text