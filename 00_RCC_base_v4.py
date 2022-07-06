#IMPORTING MODULES
import pandas
from fractions import Fraction



#FUNCTIONS
#string checker function
def string_checker(item, checker, options, error):
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
            if item.lower() in option:

                # get full name of item and put it in title
                chosen = option[0].title()
                is_valid = "yes"
                break

            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

        if is_valid != "yes":
            print(error)

        # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

#float checker function
def float_check(item, min_range, max_range, checker):
    #set variabes

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
        chosen = item
        return chosen
    else:
        return "invalid choice"

#fraction checker function
def fractions(x, units):
    characters = x.split()
    mixed_frac = "no"
    valid ="yes"

    for item in characters:
        if item.isdigit() == True:
            #check whether item is a mixed fraction (if one split value is just a number)
            num = item
            mixed_frac = "yes"

        for character in item:
            if character == "/":
                fraction = item

    #convert fraction to decimal
    try:
        fraction = float(sum(Fraction(term) for term in fraction.split()))
    #error handlign for if this cannot be done
    except:
        print("Sorry this is an invalid input")
        valid = "no"

    new_units = "g"

    #converting decimal value to grams
    if mixed_frac == "yes":
        fraction = fraction + int(num)
    if valid != "no":
        if units == "Cups":
            fraction = float(fraction) * 128
            new_units = "G"
            valid = "yes"

        elif units == "Kg":
            fraction = float(fraction) * 1000
            new_units = "G"
            valid = "yes"

        elif units == "L":
            fraction = float(fraction) * 1000
            new_units = "Ml"
            valid = "yes"

        elif units == "Tsp":
            fraction = float(fraction) * 4.2
            new_units = "G"
            valid = "yes"

        elif units == "Tbsp":
            fraction = float(fraction) * 14.85
            new_units = "G"
            valid = "yes"

        if mixed_frac != "yes":
            if fraction < 1:
                print('Sorry this amount must be positive!')
                valid = "no"

    #return values
    return fraction, new_units, valid

#amount checker function
def amount_checker(item):
    #set variavles
    amount = ""
    fraction = "no"
    unit = ""

    #check each character
    for character in item:
        if character.isalpha() == True:
            unit = unit + character
        elif character.isdigit() == True:
            amount = amount + character
        elif character == "/":
            #determine that the input is a fraction
            amount = amount + character
            fraction = "yes"
        else:
            amount = amount + character

    valid = "yes"

    #check unit is valid
    unit = string_checker(unit, "list", units, "Sorry, that is an invalid unit")

    try:
        #check amount is valid number (not negative or 0)
        amount = float_check(float(amount), 1, 2, "negative",)
    except:
        #error handling for this
        if fraction != "yes":
            print("Please enter a valid number")
            valid = "no"
    if unit == "invalid choice":
        valid = "no"
    elif amount == "invalid choice":
        valid = "no"

    new_unit = "a"

    initial_amount = str(amount)

    #converting units, if the string is said to be valid
    if valid != "no":
        if fraction == "yes" and unit != "Eggs":
            amount, new_unit, valid = fractions(amount, unit)


        elif unit == "Eggs":
            if fraction == "yes":
                print("Sorry, we don't allow fractions for amounts of eggs. Try rounding this number up!")
                valid = "no"
            if amount == 1:
                new_unit = "Egg"

        elif unit == "Kg":
            amount = float(amount) * 1000
            valid = "yes"
            new_unit = "G"
        elif unit == "L":
            amount = float(amount) * 1000
            new_unit = "Ml"
            valid = "yes"
        elif unit == "Tsp":
            amount = float(amount) * 4.2
            new_unit = "G"
            valid = "yes"
        elif unit == "Tbsp":
            amount = float(amount) * 14.8
            valid = "yes"
            new_unit = "G"
        elif unit == "Cups":
            amount = float(amount) * 128
            valid = "yes"
            new_unit = "G"
        elif unit == "G":
            amount = amount
            valid = "yes"
        elif unit == "Ml":
            new_unit = "Ml"
            valid = "yes"
        else:
            valid = "no"

        if valid != "no":
            if float(amount) < 1 and fraction != "yes":
                print('Sorry this must be a positive number!')
                valid = "no"


    #return values
    return initial_amount, unit, valid, new_unit, amount




#LISTS
yes_no = [["yes", "y"], ["no", "n"]]
units = [["kg", "kilograms", "kilogram", "kgs"], ["g", "grams", "gram", "gs"], ["ml", "millilitres", "mls"],
        ["tsp" , "teaspoon", "tsps", "teaspoons"], ["tbsp", "tablespoon", "tablespoons"], ["cups", "cup"],
        ["l", "litre", "litres"], ["eggs", "egg"]]

all_ingredients = []
amounts_needed = []
amounts_purchased = []
prices = []
#an_units =[]
#ap_units = []

#DICTIONARIES
recipe_data_dict = {
    "Ingredient": all_ingredients,
    "Amount needed": amounts_needed,
    #"Unit": an_units,
    "Amount purchased": amounts_purchased,
    #"Units": ap_units,
    "Price": prices
}


#welcome the user to the program
print("Welcome to the Recipe Cost Calculator code :)")

#ask user the name of the recipe
check_recipe = "invalid choice"
while check_recipe == "invalid choice":
    recipe = input("What is the name of your recipe : ")
    check_recipe = string_checker(recipe, "not list", yes_no, "Please enter a string input!")


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

ingredient = "yes"
while ingredient != "xxx":
    #ask user for ingredient
    check_ingredient = "invalid choice"
    while check_ingredient == "invalid choice":
        ingredient = input("Enter an ingredient needed : ")
        check_ingredient = string_checker(ingredient, "not list", yes_no, "Please enter a string input!")

    if ingredient == "xxx":
        break
    all_ingredients.append(ingredient)

    #ask user how much of ingredient is needed
    valid = "no"
    while valid == "no":
        amount_need = input("How much {} is needed in the recipe : ".format(ingredient))
        amount_need, unit, valid, an_unit, an_amount = amount_checker(amount_need)

    #amounts_needed.append(amount_need)
    #an_units.append(unit)
    amount_need_list = []
    amount_need_list.append(amount_need)
    amount_need_list.append(unit)
    amount_need = " ".join(amount_need_list)
    amounts_needed.append(amount_need)


    #ask user how much of item they purcharsed
    valid = "no"
    while valid == "no":
        amount_purchase = input("How much {} did you purcharse : ".format(ingredient))
        amount_purchase, unit, valid, ap_unit, ap_amount = amount_checker(amount_purchase)

    #amounts_purchased.append(amount_purchase)
    #ap_units.append(unit)
    amount_purchase_list = []
    amount_purchase_list.append(amount_purchase)
    amount_purchase_list.append(unit)
    amount_purchase = " ".join(amount_purchase_list)
    amounts_purchased.append(amount_purchase)

    check_ic = "invalid choice"
    #ask user how much item costed
    while check_ic == "invalid choice":
        while True:
            try:
                ingredient_cost = float(input("How much did {} cost : $".format(ingredient)))
                break
            except:
                print("Sorry, this must be a number")
        check_ic = float_check(ingredient_cost, 0, 1000, "negative")

    prices.append(ingredient_cost)



recipe_frame = pandas.DataFrame(recipe_data_dict)
recipe_frame = recipe_frame.set_index("Ingredient")
print(recipe_frame)

