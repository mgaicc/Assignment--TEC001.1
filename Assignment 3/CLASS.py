#1st Exercise
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1 

#2nd Exercise 
while True:
    inches = float(input('Enter inches to convert to centimeters: '))
    if inches > 0:
        cm = inches * 2.54
        print('Converto cm: ',cm)
    else:
        break
print('Programs ends')

#3rd Exercise
smallest = float('inf')
largest = float('-inf')

while True:
    number = input('Enter a number or empty string to quit: ')
    if number == '':
        break
    else:   
        update_number = float(number)
        smallest = min(smallest,update_number)
        largest= max(largest,update_number)
print(f'The smallest number {smallest}, the largest number {largest}')

#4th Exercise
import random
take_random = random.randint(1,10)
while True:
    user_input = int(input('Enter a number to guess: '))
    if user_input > take_random:
        print('Too high')
    elif user_input < take_random:
        print('Too low')
    else:
        print('Correct')
        break

#5th Exercise
i = 0
right_username = 'python'
right_password = 'rules'
while i < 5:
    username = input('Enter username to login ')
    password = input('Enter a password to login ')

    if username == right_username and password == right_password :
        print('Welcome')
        break
    else:
        print('You given wrong information please retry')
        i += 1
else:
    print('Access denied')

#6th Exercise
def extract_name(name):
    mid = len(name) // 2
    if len(name) % 2 == 0:
        return name[mid] + name[mid + 1]
    else:
        return name[mid]
user_name = input('Enter a string: ')
print(f'The middle character is {extract_name(user_name)}')

#7th Exercise
phrase = input('Enter a phrase: ')
def acronyms(words):   
    stored = []
    update_words = words.split()
    for char in update_words:
        stored.append((char[0].upper()))
    return ''.join(stored)
result = acronyms(phrase)
print(result)
