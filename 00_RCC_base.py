#welcome the user to the program
print("Welcome to the Recipe Cost Calculator code :)")

#ask user the name of the recipe
recipe = input("What is the name of your recipe : ")

#ask the user the serving size of the recipe
serving_size = float(input("What is the serving size of your recipe, {} : ".format(recipe)))

#ask user for ingredient
ingredient = input("Enter an ingredient needed : ")

#ask user how much of ingredient is needed
amount_need = input("How much {} is needed in the recipe : ".format(ingredient))

#ask user how much of item they purcharsed
amount_purchase = input("How much {} did you purcharse : ".format(ingredient))

#ask user how much item costed
ingredient_cost = float(input("How much did {} cost : $".format(ingredient)))

