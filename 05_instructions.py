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


yes_no = [["yes", "y"], ["no", "n"]]


check_use = "invalid choice"
while check_use == "invalid choice":
    use_program = input("Have you used this program before : ")
    check_use = string_checker(use_program, "list", yes_no, "Please enter a valid input!")

if check_use == "Yes":
    print("instructions")