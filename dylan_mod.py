from math import pi



def favorite_student():
    print("Dylan Katina")


def square_footage():
    l = int(input("What is your house's length in feet? "))
    w = int(input("What is your house's width in feet? "))
    sq = l * w
    print(f"Your houses are is {sq} square feet")


def circum():
    known = input('Do you know your circles Radius or Diameter?: ')
    if known.lower() == 'diameter':
        d = int(input('How many units long is your diameter? '))
        c = d * pi
        print(f'Your circumferenceis {c} units')
    else:
        r = int(input('How many units is your radius? '))
        b = 2 * r * pi
        print(f'Your circumferenceis {b} units')

