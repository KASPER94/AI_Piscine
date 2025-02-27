import argparse

def check_value(name, 
                cooking_lvl, cooking_time, 
                ingredients, description, 
                recipe_type):
    valid:int = 1
    if not isinstance(name, str):
        print("name of the recipe must be a string!")
        valid = 0
    try: 
        if len(name) == 0:
            valid = 0
            print("name of the recipe should not be empty")
    except TypeError:
            pass
    if not isinstance(cooking_lvl, int):
        print("cooking_lvl must be a int!")
        valid = 0
    try:
        if not 0 < cooking_lvl < 6:
            print("cooking_lvl must be between 1 and 5")
            valid = 0
    except TypeError:
        pass
    if not isinstance(cooking_time, int):
        print("cooking_time must be register!")
        valid = 0
    try:
        if not 0 > cooking_time:
            print("cooking_time must be greater than 0")
            valid = 0
    except TypeError:
        pass
    if not isinstance(ingredients, list):
        valid = 0
        print("ingredients must be given!")
    try:
        if len(ingredients) == 0:
            print("it must have at least one ingredient!")
            valid = 0
    except TypeError:
        pass
    if not isinstance(description, str):
        print("Description must be a string")
        valid = 0
    if not isinstance(recipe_type, str):
        valid = 0
        print("there must be a type for the recipe")
    try:
        if recipe_type not in ('starter', 'lunch', 'desert'):
            valid = 0
            print("the recipe must be starter, lunch or desert")
    except TypeError:
        pass
    return valid

class Recipe:
    name:str
    cooking_lvl:int
    cooking_time:int
    ingredients:list
    description:str
    recipe_type:str

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if check_value(name, 
                       cooking_lvl, cooking_time, 
                       ingredients, description, 
                       recipe_type):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        else :
            argparse.ArgumentError()

def main():
    test:str = "test"
    ingr:list = ("salade", "tomate", "ognion")
    rec = Recipe(test, 1, 10, ingr, test, "lunch")
    print(rec.name)

if __name__ == "__main__":
    main()
