#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  created_recipes = 0
  count = len(recipe)

  while(True):
    if (count == 0):
      created_recipes += 1
      count = len(recipe)

    for x in recipe:
      if (x in ingredients):
        val = ingredients[x] - recipe[x]
        if (val >= 0):
          ingredients[x] -= recipe[x]
          count -= 1
        else:
          return created_recipes
      else:
        return created_recipes

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))