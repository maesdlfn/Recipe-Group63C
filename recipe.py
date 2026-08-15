#Delfin, Cherrie Mae S. - Search
#Mariano, Julianne Cyril S. - Edit and Delete
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
    print("Recipe added successfully!")


#FEATURE - EDIT AND DELETE RECIPE

#Edit-Recipe
def edit_recipe():
    name = input("Enter recipe name to edit: ")

    for recipe in recipes:
        if recipe["name"].lower() == name.lower():
            recipe["ingredients"] = input("Enter New Ingredient: ")
            recipe["instructions"] = input("Enter New Instruction: ")
            print("Recipe Updated Successfully!")
            return

    print("Recipe not found.")


#Delete-Recipe
def delete_recipe():
    name = input("Enter recipe name to delete: ")

    for recipe in recipes:
        if recipe["name"].lower() == name.lower():
            recipes.remove(recipe)
            print("Recipe Deleted Successfully!")
            return

    print("Recipe not found.")


#SEARCH RECIPE
def search_recipe():
    name=input("Enter Food name:")

    for recipe in recipes:
        if name.lower() in recipe["name"].lower():
            print("Recipe Found!")
            print("Name:",recipe["name"])
            print("Ingredients:",recipe["ingredients"])
            print("Instructions:",recipe["instructions"])
            return

    print("Recipe not found.")


#VIEW ALL FOODS
def view_all_foods():
    print("\n------ FOOD RECIPES ------")

    if len(recipes) == 0:
        print("No recipes available.")
        return

    for recipe in recipes:
        print("Name:", recipe["name"])
        print("Ingredients:", recipe["ingredients"])
        print("Instructions:", recipe["instructions"])
        print("------------------------")


#MAIN MENU
while True:

    print("\nRECIPE")
    print("1. Add Recipe")
    print("2. Edit Recipe")
    print("3. Delete Recipe")
    print("4. Search Recipe")
    print("5. View All Foods")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_recipe()

    elif choice == "2":
        edit_recipe()

    elif choice == "3":
        delete_recipe()

    elif choice == "4":
        search_recipe()

    elif choice == "5":
        view_all_foods()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

    if choice != "6":
        input("\nPress 0 to go back to main page...")