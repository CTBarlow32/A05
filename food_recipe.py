'''
Carter Barlow
IS303 - A05
Food Recipe Book

This program mirrors a recipe book that hold recipes.
Chef can add recipes, see list of recipes, and find longest recipe to make

Inputs:
- Name of Recipe
- Ingredients
- Category of Food
- Time to Make Food

Processes:
Recipe Book Class: stores recipes in list, adds recipes, calculates longest recipe to make, displays all recipes
Recipe Class: Name, Ingredients, Time to make, category of food

Outputs: Each recipes info, recipes in order of category, longest recipe to make
'''

class recipe:
    def __init__(self, name, ingredients, time, category):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.ingredients} - {self.time} min"


class recipe_book:
    def __init__ (self, name):
        self.name = name
        self.recipes = []

    def add_recipe(self, recipe):
        '''Add recipe to recipe book '''
        self.recipes.append(recipe)

    def get_average_minutes(self):
        '''Return average minutes for all recipes'''
        if len(self.recipes) == 0:
            return 0
        total = sum(recipe.time for recipe in self.recipes)
        return total / len(self.recipes)
    
    def get_longest (self):
        '''Return recipe with longest time to make'''
        if len(self.recipes) == 0:
            return None
        longest = self.recipes[0]
        for recipe in self.recipes:
            if recipe.time > longest.time:
                longest = recipe
        return longest
    
    def __str__ (self):
        header = f"Recipe Book: {self.name} ({len(self.recipes)}) recipes"
        recipe_list = ""
        for recipe in self.recipes:
            recipe_list = recipe_list + f"\n - {recipe}"
        return header + recipe_list
    

# Central Flow

book = recipe_book ("The most delicious") #???

book.add_recipe(recipe("Lasagana" , "Tomato Sauce, Pasta, Beef, Cheese" , 60 , "Entree"))
book.add_recipe(recipe("Jello", "Jello Packet, Water", 10, "Dessert"))
book.add_recipe(recipe("Bread Sticks", "Bread Dough, Butter", 45, "Side"))

print(book)
print(f"\n Average time: {book.get_average_minutes():.0f} minutes")

longest = book.get_longest()
print(f"Longest Recipe: {longest.name} {longest.time} minutes")