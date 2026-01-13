#Exercise 1
name = input('Enter your name: ')
print(f'Hello {name}!')

#Exercise 2
import math
radius = float(input('Enter your radius: '))
circumference = 2* math.pi * radius
print(f'Circumference: {circumference:.2f}')

#Exercise 3
length = float(input('Enter your length: '))
width = float(input('Enter your width: '))
if length < width:
  print('Cannot calculate because rectangle require length > width')
else:
  area = length * width
  circumference = 2 * (width + length)
  print(f'Area: {area}')
  print(f'Circumference: {circumference}')

#Exercise 4
first_number = int(input('Enter your first number: '))
second_number = int(input('Enter your second number: '))
third_number = int(input('Enter your third number: '))
total = first_number + second_number + third_number
average = (total/ 3)
product = first_number * second_number * third_number
print(f'Sum: {total}')
print(f'Average: {average}')
print(f'Product: {product}')

#Exercise 5
talents =float(input('Enter your talents: '))
pounds = float(input('Enter your pounds: '))
lots = float(input('Enter your lots: '))
talents_to_pounds = talents * 20
pounds_to_talents = (pounds + talents_to_pounds) * 32
lots_to_grams = (lots + pounds_to_talents) * 13.3
kilograms = int(lots_to_grams * 0.001)
grams = lots_to_grams - (kilograms * 1000)
print(f'{kilograms} Kilograms and {grams:.2f} grams')

#Exercise 6
import random
r1 = random.randint(0, 9)
r2 = random.randint(0, 9)
r3 = random.randint(0, 9)
print(f'3 digit code: {r1}{r2}{r3}')

n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
n3 = random.randint(1, 6)
n4 = random.randint(1, 6)
print(f'4 digit code:{n1}{n2}{n3}{n4}')
