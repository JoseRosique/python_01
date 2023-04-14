# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 17:51:26 by joslopez          #+#    #+#              #
#    Updated: 2023/04/13 21:50:53 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book

if __name__ == '__main__':
    listy = ['Bread', 'Milk', 'Chocolate']
    cake = Recipe("Cake", 3, 20, listy, "", "dessert")
    
    listy = ['Turkey', 'Lettuce', 'Potatoes']
    sandwich = Recipe("Sandwich", 3, 10, listy, "A good sandwich", "lunch")
    
    first_book = Book("First book")
    
    first_book.add_recipe(cake)
    first_book.add_recipe(sandwich)
    
    Book.get_recipes_by_types(first_book, 'lunch')
    print("")
    Book.get_recipes_by_types(first_book, 'dessert')
    print("")
    print(sandwich)
    print("")
    print(cake)
    