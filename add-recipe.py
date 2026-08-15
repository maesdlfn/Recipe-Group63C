#ADD RECIPE

recipes =[]

def add_recipe():
    name=input("Enter recipe name:")
    ingredients=input("Enter Ingredients:")
    instructions=input("Enter Instructions:")

    recipe = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions

    }
    recipes.append(recipe)
print("recipe add successfully")

add_recipe()

