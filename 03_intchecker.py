#set up int checker function
def int_check(item, min_range, max_range ):
    #set variabes
    is_valid = ""
    chosen = ""
    #set variabes
    is_valid = ""
    chosen = ""

    #running the string checker when not checking a string is in a list
    # if item is not blank, program continues
    if item > min_range and item <= max_range:
        chosen = "valid"
        is_valid = "yes"
        # if item is blank, show error (& repeat loop)
    elif item < 1:
        print("Sorry, this value has to be a positive integer")
    else:
        print("Sorry, this is not a valid number!")



    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"




check_num = "invalid choice"
while check_num == "invalid choice":
    number = int(input("Enter a number : "))
    check_num = int_check(number, 0, 1000)














