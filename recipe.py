#Delfin, Cherrie Mae S. - Search
#Mariano, Juliannae Cyril S. - Edit and Delete
#Padilla, Mark Jay B. - Search

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

#FEATURE - EDIT AND DELETE RECIPE

#Edit-Recipe
def edit_recipe():
    name = input ("enter recipe name to edit: ")

    for recipe in recipes:
        if recipe ["name"].lower()==name.lower():
            recipe["ingredients"] = input ("Enter New Ingredient: ")
            recipe["instructions"] = input ("Enter New Instrcution: ")
            print ("Recipe Updated Succesfully!")
        return


#Delete-Recipe
def delete_recipe():
    name = input ("enter recipe name to delete: ")

    for recipe in recipes:
        if recipe ["name"].lower()==name.lower():
            recipes.remove(recipe)
            print ("Recipe Deleted Succesfully!")
        return


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

add_recipe()
edit_recipe()
search_recipe()
delete_recipe()
