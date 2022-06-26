

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

def question():
    check_amount = "invalid choice"
    while check_amount == "invalid choice":
        amount = input("Amount : ")
        check_amount = string_checker(amount, "not list", yes_no)
    return amount

yes_no = [["yes", "y"], ["no", "n"]]
units = [["kg", "kilograms", "kilogram", "kgs"], ["g", "grams", "gram", "gs"], ["ml", "millilitres","mls"],
         ["tsp", "teaspoon", "tsps", "teaspoons"], ["tbsp", "tablespoon", "tablespoons"],["cups", "cup"],
         ["l", "litre", "litres"]]

def amount_checker():
    check_amount = "invalid choice"
    while check_amount == "invalid choice":
        amount = input("Amount : ")
        check_amount = string_checker(amount, "not list", yes_no)

        if check_amount != "invalid choice":
            check_split = "invalid choice"
            while check_split == "invalid choice":
                while True:
                    try:
                        amount_split = amount.split()
                        amount_num = amount_split[0]
                        amount_unit = amount_split[1]
                        amount_num_check = float_check(float(amount_num), 0, 1, "negative")
                        check_split = "no"
                        break
                    except:
                        print("Invalid input")
                        check_amount = "invalid choice"
                        while check_amount == "invalid choice":
                            amount = input("Amount : ")
                            check_amount = string_checker(amount, "not list", yes_no)

            amount_unit_check = string_checker(amount_unit, "list", units)
            amount_num_check = float_check(float(amount_num), 0, 1, "negative")

            while amount_unit_check == "invalid choice" or amount_num_check == "invalid choice":
                amount = question()
                while True:
                    try:
                        amount_split = amount.split()
                        amount_num = amount_split[0]
                        amount_unit = amount_split[1]
                        check_split = "no"
                        break
                    except:
                        print("Invalid input")
                        check_amount = "invalid choice"
                        while check_amount == "invalid choice":
                            amount = input("Amount : ")
                            check_amount = string_checker(amount, "not list", yes_no)

                amount_unit_check = string_checker(amount_unit, "list", units)
                amount_num_check = float_check(float(amount_num), 0, 1, "negative")



    amount_unit = amount_unit_check

    if amount_unit == "Kg":
        amount_num = float(amount_num)*1000
        amount_unit = "G"
    elif amount_unit == "Tsp":
        amount_num = float(amount_num) * 4.2
        amount_unit = "G"

    elif amount_unit == "Tbsp":
        amount_num = float(amount_num) * 14.8
        amount_unit = "G"

    elif amount_unit == "L":
        amount_num = float(amount_num) * 1000
        amount_unit = "Ml"

    return amount_num, amount_unit



number, unit = amount_checker()

print(number)
print(unit)