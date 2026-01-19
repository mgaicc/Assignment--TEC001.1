#1st Exercise
def zander_length(length):
    if length >= 42:
        print('You have successfully catch the fish')
    else:
        different = 42 - length
        print('Your zander to short, you have to release the fish')
        print(f'Your zander below the size limit is {different}')
try:
    asking_length = float(input('Please enter zander length in centimeter: '))
    zander_length(asking_length)
except ValueError:
    print('Please enter a valid zander length')
#2nd Exercise
def cabin_class(model):
    if model == 'LUX':
        print('Your cabin class is upper-deck cabin with a balcony')
    elif model == 'A':
        print('Your cabin class is above car deck, equipped with a window')
    elif model == 'B':
        print('Your cabin class is windowless cabin above the car deck')
    elif model == 'C':
        print('Your cabin class is windowless cabin below the car deck')
    else:
       print('Invalid cabin class')
cabin = input('Enter your cabin class:').upper()
cabin_class(cabin)
#3rd exercise
def health_judge():
    sex = input('Enter your biological sex: ')
    try:
        hemoglobin = int(input('Enter your hemoglobin value (g/l): '))
    except ValueError:
        print('Please enter a numeric value')
        return
    if sex == 'male':
        if hemoglobin < 134:
            print('Your hemoglobin is low')
        elif 134<= hemoglobin <= 167:
            print('Your hemoglobin is normal')
        else:
            print('Your hemoglobin is high')
    elif sex == 'female':
        if hemoglobin < 117:
            print('Your hemoglobin is low')
        elif 117<= hemoglobin <=155:
            print('Your hemoglobin is normal')
        else:
            print('Your hemoglobin is high')
health_judge()
#4th Exercise
def leap_year():
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
    else:
        print("Not a leap year")
leap_year()
#5th Exercise
import math
def pizza_receiver(diameter,price):
    conver_to_meters = (diameter/2) * 0.01
    area_of_pizza = conver_to_meters ** 2 * math.pi
    return price / area_of_pizza
try:
    d1 = float(input("Enter the diameter of the pizza in centimeters: "))
    d2 = float(input("Enter the diameter of the pizza in centimeters: "))

    p1 = float(input("Enter the price of the pizza in USD: "))
    p2 = float(input("Enter the price of the pizza in USD: "))

    unit_price1 = pizza_receiver(d1,p1)
    unit_price2 = pizza_receiver(d2,p2)
    print('\nResult')
    print(f'Pizza 1 {unit_price1:.2f} per square meters')
    print(f'Pizza 2 {unit_price2:.2f} per square meters')
    if unit_price1 > unit_price2:
        print('\n The second pizza have a better money value')
    elif unit_price1 < unit_price2:
        print('\n The first pizza have a better money value')
    else:
        print('\n Both pizza have the same money value')
except ValueError:
    print('Please enter a numeric value')