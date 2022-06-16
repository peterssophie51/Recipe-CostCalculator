#set up float checker function
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
        if item < 1:
            print("Sorry, this value has to be a positive number")
        else:
            print("Sorry this is not a valid number!")




    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"




check_num = "invalid choice"
while check_num == "invalid choice":
    while True:
        try:
            number = float(input("Enter a number : "))
            break
        except:
            print("Sorry, this must be a number")
    check_num = float_check(number, 0, 1000, "range")


check_num2 = "invalid choice"
while check_num2 == "invalid choice":
    while True:
        try:
            number2 = float(input("Enter a second number : "))
            break
        except:
            print("Sorry, this must be a number")
    check_num2 = float_check(number2, 0, 1000, "negative")















