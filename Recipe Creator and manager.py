import sys

#Recipe is a representation of a cooking recipe
class Recipe:
   def __init__(self):
       self.ingredients=[]
       self.instructions=[]
       self.name=" "
#save/store it into dictionary ,Test it
def  create():
    recipe=Recipe()
    recipe_dict={}

    print("create a recipe!")
    recipe.name=input("Recipe Nmae:")


    while True:
        ingredients=input("Ingredients:")
        if ingredients == 'exit':
            break
        recipe.ingredients.append(ingredients)

    while True:
        instructions=input("Instructions:")
        if instructions == 'exit':
            break
        recipe.instructions.append(instructions)

    recipe_dict[recipe.name]=recipe

def listrecipe():
    print('listrecipe')

def update():
    print("update")

def delete():
    print("delete")

def main():
    if len(sys.argv)!=2:
        print("Usage: recipe <Action>[args]")
        sys.exit(1)

    action=sys.argv[1]

    if "create"==action:
        create()
    elif "list"==action:
        listrecipe()
    elif "update"==action:
        update()
    elif "delete"==action:
        delete()
    else:
        print("command not found")

main()



