#FUNCTIONS
#string checker function
def string_checker(item, checker, options):
    #set variabes
    is_valid = ""
    chosen = ""

    #running the string checker when not checking a string is in a list
    if checker == "not list":
        # if item is not blank, program continues
        if item != "":
            chosen = "valid"
            is_valid = "yes"
            # if item is blank, show error (& repeat loop)
        else:
            print("Sorry - this can’t be blank!")


    elif checker == "list":

        for option in options:

            # if the item is in one of the lists, return the full name of the item
            if item in option:

                # get full name of item and put it in title
                chosen = option[0].title()
                is_valid = "yes"
                break

            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

        if is_valid != "yes":
            print("Please enter a valid option")

        # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

#float checker function
def float_check(item, min_range, max_range, checker):
    #set variabes

    is_valid = ""
    chosen = ""
    #set variabes
    is_valid = ""
    chosen = ""
    if checker == "range":
        #running the string checker when not checking a string is in a list
        # if item is not blank, program continues
        if item > min_range and item <= max_range:
            chosen = "valid"
            is_valid = "yes"
            # if item is blank, show error (& repeat loop)
        elif item < 1:
            print("Sorry, this value has to be a positive number")
        else:
            print("Sorry, this is not a valid number!")
    elif checker == "negative":
        if item > 0:
            is_valid = "yes"
        elif item < 1:
            print("Sorry, this value has to be a positive number")
        else:
            print("Sorry this is not a valid number!")




    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"





#LISTS
yes_no = [["yes", "y"], ["no", "n"]]





#welcome the user to the program
print("Welcome to the Recipe Cost Calculator code :)")

#ask user the name of the recipe
check_recipe = "invalid choice"
while check_recipe == "invalid choice":
    recipe = input("What is the name of your recipe : ")
    check_recipe = string_checker(recipe, "not list", yes_no)


#ask the user the serving size of the recipe
check_ss = "invalid choice"
while check_ss == "invalid choice":
    while True:
        try:
             serving_size = float(input("What is the serving size of your recipe, {} : ".format(recipe)))
             break
        except:
            print("Sorry, this must be a number")
    check_ss = float_check(serving_size, 0, 1000, "negative")

#ask user for ingredient
check_ingredient = "invalid choice"
while check_ingredient == "invalid choice":
    ingredient = input("Enter an ingredient needed : ")
    check_ingredient = string_checker(ingredient, "not list", yes_no)

#ask user how much of ingredient is needed
amount_need = input("How much {} is needed in the recipe : ".format(ingredient))

#ask user how much of item they purcharsed
amount_purchase = input("How much {} did you purcharse : ".format(ingredient))

#ask user how much item costed
while check_ic == "invalid choice":
    while True:
        try:
            ingredient_cost = float(input("How much did {} cost : $".format(ingredient)))
            break
        except:
            print("Sorry, this must be a number")
    check_ic = float_check(ingredient_cost, 0, 1000, "negative")


