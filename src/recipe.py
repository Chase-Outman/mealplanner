from enum import Enum

class Recipe():
    def __init__(self, name, ingredients, intructions = None):
        self.name = name
        self.ingredients = ingredients
        self.intructions = intructions

    def __str__(self):
        return f"{self.name}\n\n{'\n'.join(str(ingredient) for ingredient in self.ingredients)}\n\n{'\n'.join(self.intructions)}"
    
    def print_recipe(self):
        print(self)
        
class UnitType(Enum):
    CUPS='cups'
    TEASPOON = 'teaspoon'
    TABLESPOON = 'tablespoon'
    POUND = 'pound'
    UNIT = ''
    

class Ingredient():
    def __init__(self, name, units, unit_type):
        self.name = name
        self.units = units
        self.unit_type = unit_type
    
    def __str__(self):
        if self.unit_type == UnitType.UNIT:
            return f"\t{self.units}{self.unit_type.value} {self.name}"
        return  f"\t{self.units} {self.unit_type.value} of {self.name}"