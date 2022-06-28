from fractions import Fraction

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
            if item.lower() in option:

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
def fractions(x, units):
    characters = x.split()
    mixed_frac = "no"
    for item in characters:
        if item.isdigit() == True:
            num = item
            mixed_frac = "yes"

        for character in item:
            if character == "/":
                fraction = item

    fraction = float(sum(Fraction(term) for term in fraction.split()))

    if mixed_frac == "yes":
        fraction = fraction + int(num)

    if units == "Cups":
        fraction = float(fraction) * 128
        units = "G"

    elif units == "Kg":
        fraction = float(function) * 1000
        units = "G"

    elif units == "L":
        fraction = float(fraction) * 1000
        units = "Ml"

    elif units == "Tsp":
        fraction = float(fraction) * 4.2
        units = "G"

    elif units == "Tbsp":
        fraction = float(fraction) * 14.85
        units = "G"

    return fraction, units

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

    unit = string_checker(unit, "list", units)

    if fraction == "yes":
        amount, unit = fractions(amount, unit)

    if unit == "Kg":
        amount = float(amount) * 1000
        unit = "G"
    elif unit == "L":
        amount = float(amount) * 1000
        unit = "Ml"
    elif unit == "Tsp":
        amount = float(amount) * 4.2
        unit = "G"
    elif unit == "Tbsp":
        amount = float(amount) * 14.8
    elif unit == "Cups":
        amount = float(amount) * 128



    return amount, unit

units = [["kg", "kilograms", "kilogram", "kgs"], ["g", "grams", "gram", "gs"], ["ml", "millilitres", "mls"],
        ["tsp" , "teaspoon", "tsps", "teaspoons"], ["tbsp", "tablespoon", "tablespoons"], ["cups", "cup"],
        ["l", "litre", "litres"]]

x = input("Amount : ")
amount, unit = amount_checker(x)
print(amount)
print(unit)