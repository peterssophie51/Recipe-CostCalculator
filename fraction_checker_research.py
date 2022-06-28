from fractions import Fraction

x =input("Enter a fraction please : ")

def fractions(x):
    characters = x.split()
    for item in characters:
        if item.isdigit() == True:
            num = item
            mixed_frac = "yes"

        for character in item:
            if character == "/":
                fraction = item


    print(characters)
    fraction = float(sum(Fraction(term) for term in fraction.split()))
    if mixed_frac == "yes":
        fraction = fraction + int(num)
    fraction *= 128

    return fraction

print(fractions(x))
