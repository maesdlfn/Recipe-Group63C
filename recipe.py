#Delfin, Cherrie Mae S.

#SEARCH RECIPE
def search_recipe():
    name=input ("Enter Food name:")

    for recipe in recipes:
        if name.lower() in recipe["name"].lower():
            print("Recipe Found!")
            print("Name:",recipe["name"])
            print("Ingredients:",recipe["ingredients"])
            print("Instructions:",recipe["instructions"])
            return

            print("Recipe not found.")