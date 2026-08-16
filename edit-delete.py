#FEATURE - EDIT AND DELETE RECIPE

#Edit-Recipe
def edit_recipe():
    name = input ("enter recipe name to edit: ")

    for recipe in recipes:
        if recipe ["name"].lower()==name.lower():
            new_ingredients = input ("Enter New Ingredient:")
            new_instructions = input ("Enter New Instrcution:")

            recipe["ingredients"] += "," + new_ingredients
            recipe["instructions"] += "," + new_instructions
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

edit_recipe()
delete_recipe()
    


