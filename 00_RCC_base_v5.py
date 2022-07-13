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

def space(number):
    for i in range(number):
        print()




#LISTS
yes_no = [["yes", "y"], ["no", "n"]]
units = [["kg", "kilograms", "kilogram", "kgs"], ["g", "grams", "gram", "gs"], ["ml", "millilitres", "mls"],
        ["tsp" , "teaspoon", "tsps", "teaspoons"], ["tbsp", "tablespoon", "tablespoons"], ["cups", "cup"],
        ["l", "litre", "litres"], ["eggs", "egg"]]

all_ingredients = []
amounts_needed = []
amounts_purchased = []
prices = []
total_price = 0
serving_price = 0
#an_units =[]
#ap_units = []
recipes = []
serving = []
total = []

#DICTIONARIES
recipe_data_dict = {
    "Ingredient": all_ingredients,
    "Amount needed": amounts_needed,
    "Amount purchased": amounts_purchased,
    "Price": prices
}

costs_dict = {
    "": recipes,
    "Serving" : serving,
    "Total"   : total
}


#welcome the user to the program
print("Welcome to the Recipe Cost Calculator code :)")
space(1)
check_use = "invalid choice"
while check_use == "invalid choice":
    use_program = input("Have you used this program before : ")
    check_use = string_checker(use_program, "list", yes_no, "Please enter a valid input!")

if check_use == "No":
    print("The program you’re using is a simple, easy to use program, that will calculate both the total price\n"
          "and serving price for any recipe.")
    space(1)
    print("There’s just a few things you’ll need to know before running this program!")
    space(1)
    print("When the program asks for you to enter the ingredient, this just means the name of the\n"
          "ingredient, for example, “Butter” or “Flour”. You will then be prompted to first, enter the\n"
          "amount needed and then the amount purchased. Amount needed means the amount you\n"
          "need in the recipe (for example to make cake you may need 1 ½ cups of flour). Amount\n"
          "purchased means the amount of the ingredient you purchased from the store, for example\n"
          "the flour may have come in a 1.5kg package. Price just refers to the price of what you purchased!")
    space(1)
    print('You also cannot enter fractions in terms of the amount of eggs (for example ½ Egg)')
    space(1)
    print("Some things to note in this program :")
    space(1)
    print("If eggs is one of your ingredients, you will need to make sure eggs are entered as a unit,\n"
          "when inputting the amount needed and amount purchased (for example “2 Eggs”).")
    space(1)
    print("The program will only convert the cup measurements into grams, as it can not determine \n"
          "whether the ingredient is liquid or solid. This also means there is no function that will check \n"
          "that the unit for amount needed and amount purchased is the same (once converted), and it \n"
          "is assumed that 1 ml = 1 g.")
    space(1)
    print("This program uses a base value when converting cup measurements to grams as well, \n"
          "meaning that when converting this would be affected by the density of the ingredient. I \n"
          "cannot determine the density of an ingredient, so for this program I have used a set number. \n"
          "This is the same for teaspoon and tablespoon, as this conversion uses a general number, \n"
          "not based on density.")
    space(1)
    print("This program will run a loop that will continue to ask you to enter the ingredients in the \n"
          "recipe, and then questions following that, which will provide it with enough information on the \n"
          "ingredient. To exit this loop, once you have finished entering in your ingredients and other \n"
          "information, you will need to type “xxx” when prompted to enter an ingredient. ")



space(2)

#ask user the name of the recipe
check_recipe = "invalid choice"
while check_recipe == "invalid choice":
    recipe = input("What is the name of your recipe : ")
    check_recipe = string_checker(recipe, "not list", yes_no, "Please enter a string input!")

recipes.append(recipe)

space(1)
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

space(2)
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

    space(1)

    #ask user how much of ingredient is needed
    valid = "no"
    while valid == "no":
        amount_need = input("How much {} is needed in the recipe : ".format(ingredient))
        amount_need, unit, valid, an_unit, an_amount = amount_checker(amount_need)

    space(1)

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
        amount_purchase = input("How much {} did you purchase : ".format(ingredient))
        amount_purchase, unit, valid, ap_unit, ap_amount = amount_checker(amount_purchase)

    space(1)

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
        space(2)




    prices.append(ingredient_cost)

    ingredient_price = ingredient_cost / ap_amount
    ingredient_price = an_amount * ingredient_price
    total_price += ingredient_price

serving_price = total_price / serving_size
serving.append("{:.2f}".format(serving_price))
total.append("{:.2f}".format(total_price))


recipe_frame = pandas.DataFrame(recipe_data_dict)
recipe_frame = recipe_frame.set_index("Ingredient")

cost_frame = pandas.DataFrame(costs_dict)
cost_frame = cost_frame.set_index("")

space(2)
print(recipe)
space(1)
print(recipe_frame)
space(2)
print(cost_frame)



