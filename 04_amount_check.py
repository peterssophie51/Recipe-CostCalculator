import re

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

units = [["kg", "kilograms", "kilos"], ["grams", "g"]]



check_amount = "invalid choice"
while check_amount == "invalid choice":
    print('When entering an amount, please make sure to use a space between your number and input')
    amount = input("Amount : ")
    amount_split = re.split('\s|(?<!\d)[,.](?!\d)', amount)
    print(amount_split)
    number = amount_split[0]
    unit = amount_split[1]
    check_amount = string_checker(unit, "list", units)

check_amount = unit
if unit == "kg" or unit == "kilograms" or unit == "kilos":
    numberint = float(number)*1000
else:
    numberint = number


print(numberint)


