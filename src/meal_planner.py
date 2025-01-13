from utility import load_objects, save_object
import random

class MealPlanner():    
    def __init__(self):
        self.recipes = load_objects('test_recipe.pkl')
        self.remaining_recipes = self.recipes.copy()
        self.meal_plan = {}


    def generate_meal_plan(self): 
        #randomizes the remaining recipe list so that each generate is different 
        self.remaining_recipes = random.sample(self.remaining_recipes, k=len(self.remaining_recipes))      
        for i in range(1,8):
            self.meal_plan[i] = self.remaining_recipes.pop()

    def print_meal_plan(self):
        for day in self.meal_plan:
            print(f"{day}: {self.meal_plan[day].name}")