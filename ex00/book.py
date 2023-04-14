# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 17:51:34 by joslopez          #+#    #+#              #
#    Updated: 2023/04/13 21:46:13 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
        
    def __str__(self):
        txt += "Recipe book's name:" + self.name + '\n'
        txt += "Last update:" + str(self.last_update) + '\n'
        txt += "Creation date:" + str(self.creation_date) + '\n'
        txt += "Starters:" + str(self.recipes_list['starter']) + '\n'
        txt += "Lunches:" + str(self.recipes_list['lunch']) + '\n'
        txt += "Desserts:" + str(self.recipes_list['dessert']) + '\n'
        return txt
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name texttt{name} and returns the instance"""
        if isinstance(name. str):
            for lst in self.recipes_list.values():
                for item in lst:
                    if item.name == name:
                        print(item)
                        return item
            print("Couldn't find the recipe you were looking for.")
        else:
            print("Error: Name must be a string.")
        exit()
        
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if isinstance(recipe_type, str):
            if recipe_type in self.recipes_list:
                print("Recipes in " + recipe_type + " :")
                for item in self.recipes_list[recipe_type]:
                    print(item.name)
                return
            else:
                print("Error: Recipe type isn't starter, lunch or dessert.")
        else:
            print("Error: Recipe type must be a string.")
            exit()
            
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if recipe.recipe_type in self.recipes_list:
                self.recipes_list[recipe.recipe_type].append(recipe)
                self.last_update = datetime.now()
            else:
                print("Error: Recipe type must be starter, lunch or dessert.")
        else:
            print("Error: Recipe isn't an instance of the Recipe class.")
            exit()