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

if check_use == "No":
    print("The program you’re using is a simple, easy to use program, that will calculate both the total price\n"
          "and serving price for any recipe.")
    print()
    print("There’s just a few things you’ll need to know before running this program!")
    print()
    print("When the program asks for you to enter the ingredient, this just means the name of the\n"
          "ingredient, for example, “Butter” or “Flour”. You will then be prompted to first, enter the\n"
          "amount needed and then the amount purchased. Amount needed means the amount you\n"
          "need in the recipe (for example to make cake you may need 1 ½ cups of flour). Amount\n"
          "purchased means the amount of the ingredient you purchased from the store, for example\n"
          "the flour may have come in a 1.5kg package. Price just refers to the price of what you purchased!")
    print()
    print('You also cannot enter fractions in terms of the amount of eggs (for example ½ Egg)')
    print()
    print("Some things to note in this program :")
    print()
    print("If eggs is one of your ingredients, you will need to make sure eggs are entered as a unit,\n"
          "when inputting the amount needed and amount purchased (for example “2 Eggs”).")
    print()
    print("The program will only convert the cup measurements into grams, as it can not determine \n"
          "whether the ingredient is liquid or solid. This also means there is no function that will check \n"
          "that the unit for amount needed and amount purchased is the same (once converted), and it \n"
          "is assumed that 1 ml = 1 g.")
    print()
    print("This program uses a base value when converting cup measurements to grams as well, \n"
          "meaning that when converting this would be affected by the density of the ingredient. I \n"
          "cannot determine the density of an ingredient, so for this program I have used a set number. \n"
          "This is the same for teaspoon and tablespoon, as this conversion uses a general number, \n"
          "not based on density.")
    print()
    print("This program will run a loop that will continue to ask you to enter the ingredients in the \n"
          "recipe, and then questions following that, which will provide it with enough information on the \n"
          "ingredient. To exit this loop, once you have finished entering in your ingredients and other \n"
          "information, you will need to type “xxx” when prompted to enter an ingredient. ")