from fractions import Fraction
valid = "no"
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
def fractions(x, units):
    characters = x.split()
    mixed_frac = "no"
    valid ="yes"

    for item in characters:
        if item.isdigit() == True:
            num = item
            mixed_frac = "yes"

        for character in item:
            if character == "/":
                fraction = item
    try:
        fraction = float(sum(Fraction(term) for term in fraction.split()))
    except:
        print("Sorry this is an invalid input")
        valid = "no"


    if mixed_frac == "yes":
        fraction = fraction + int(num)
    if valid != "no":
        if units == "Cups":
            fraction = float(fraction) * 128
            units = "G"
            valid = "yes"

        elif units == "Kg":
            fraction = float(fraction) * 1000
            units = "G"
            valid = "yes"

        elif units == "L":
            fraction = float(fraction) * 1000
            units = "Ml"
            valid = "yes"

        elif units == "Tsp":
            fraction = float(fraction) * 4.2
            units = "G"
            valid = "yes"

        elif units == "Tbsp":
            fraction = float(fraction) * 14.85
            units = "G"
            valid = "yes"

        if mixed_frac != "yes":
            if fraction < 1:
                print('Sorry this amount must be positive!')
                valid = "no"

    return fraction, units, valid

def amount_checker(item):
    amount = ""
    fraction = "no"
    unit = ""
    for character in item:
        if character.isalpha() == True:
            unit = unit + character
        elif character.isdigit() == True:
            amount = amount + character
        elif character == "/":
            amount = amount + character
            fraction = "yes"
        else:
            amount = amount + character

    valid = "yes"

    unit = string_checker(unit, "list", units, "Sorry, that is an invalid unit")
    try:
        amount = float_check(float(amount), 1, 2, "negative",)
    except:
        if fraction != "yes":
            print("Please enter a valid number")
            valid = "no"
    if unit == "invalid choice":
        valid = "no"
    elif amount == "invalid choice":
        valid = "no"



    if valid != "no":
        if fraction == "yes":
            amount, unit, valid = fractions(amount, unit)

        elif unit == "Kg":
            amount = float(amount) * 1000
            valid = "yes"
            unit = "G"
        elif unit == "L":
            amount = float(amount) * 1000
            unit = "Ml"
            valid = "yes"
        elif unit == "Tsp":
            amount = float(amount) * 4.2
            unit = "G"
            valid = "yes"
        elif unit == "Tbsp":
            amount = float(amount) * 14.8
            valid = "yes"
            unit = "G"
        elif unit == "Cups":
            amount = float(amount) * 128
            valid = "yes"
            unit = "G"
        elif unit == "G":
            amount = amount
            valid = "yes"
        else:
            valid = "no"

        if valid != "no":
            if float(amount) < 1 and fraction != "yes":
                print('Sorry this must be a positive number!')
                valid = "no"



    return amount, unit, valid

units = [["kg", "kilograms", "kilogram", "kgs"], ["g", "grams", "gram", "gs"], ["ml", "millilitres", "mls"],
        ["tsp" , "teaspoon", "tsps", "teaspoons"], ["tbsp", "tablespoon", "tablespoons"], ["cups", "cup"],
        ["l", "litre", "litres"]]
valid = "no"
while valid == "no":
    x = input("Amount : ")
    amount, unit, valid = amount_checker(x)
print(amount)
print(unit)