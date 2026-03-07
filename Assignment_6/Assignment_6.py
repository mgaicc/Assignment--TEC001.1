#1st Exercises
store = []
while True:
    user_num = input('Enter your to sorted or press space to end:')
    if user_num == '':
        break
    else:
        update_num = float(user_num)
        store.append(update_num)
store.sort(reverse=True)
top_five = store[:5]
print(f'Five greatest number in descending order')
for num in top_five:
    print(num)
#2nd Exercises
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter the number of a month (1-12): "))
if month < 1 or month > 12:
    print("Invalid month! Please enter a number between 1 and 12.")
else:
    if month in (12, 1, 2):
        season = seasons[0] 
    elif month in (3, 4, 5):
        season = seasons[1]  
    elif month in (6, 7, 8):
        season = seasons[2] 
    else:
        season = seasons[3]  
    
    print(f"The season is {season}.")
#3rd Exercises
names = set()
while True:
    name = input('Enter your name: ')
    if name == '':
        break
    if name in names:
        print('Exisiting name')
    else:
        print('New name')
        names.add(name)
for name in names:
    print(name)

#4th Exercises
def frequency_words(sentences):
    words = {}
    for word in sentences.strip():
        if word not in words:
            words[word] = 0
            words[word] += 1
        else:
            words[word] += 1
    return words
sentence = input('Enter your sentences: ')
print(frequency_words(sentence))

#5th Exercises
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def list_parameter(contain):
    new_contain = []
    for num in contain:
        if num % 2 == 0:
            new_contain.append(num)
    return new_contain
def cut_down(contain):
    new_cut_down_contain = []
    for num in contain:
        if num % 2 == 1:
            new_cut_down_contain.append(num)
    return new_cut_down_contain
result = list_parameter(test)
cut_down_store = cut_down(test)
print(f'The original list {test}')
print(f'The second list {result}')
print(f'The cut down list {cut_down_store}')

#6th Exercises
import random

def estimate_pi(num_points):
    inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / num_points
    
    return pi_estimate
num_points = int(input("How many random points to generate? "))
pi_approx = estimate_pi(num_points)

print(f"\nWith {num_points:,} random points:")
print(f"Approximation of π: {pi_approx}")