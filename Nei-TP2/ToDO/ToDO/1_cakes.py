"""Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out,
how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). 
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""
def cakes(recipe, available):

    cake_count = []
    
    for ingredient, quantity in recipe.items():
        if ingredient not in available:
            return 0  # Ingredient missing, can't make the cake

        cake_count.append(available[ingredient] // quantity)

    return min(cake_count)



def main():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200} 
    print(cakes(recipe, available)) # Deve printar 2

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000} # Deve printar 0
    print(cakes(recipe, available))

    recipe = {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}
    print(cakes(recipe, available)) # Deve printar 11

if __name__ == "__main__":
    main()