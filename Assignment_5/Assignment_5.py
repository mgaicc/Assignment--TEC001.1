#1st Exercise.
store = []
while True:
    user_input = input('Enter a number or press enter to quit: ')
    if user_input == '':
        break
    else:
        up_user_input = int(user_input)
        store.append(up_user_input)
store.sort(reverse=True)
print(store[:6])

#2nd Exercises
def is_prime(contain):
    if contain < 2:
        print(f'{contain} Is not prime number')
    for i in range(2,int(contain**0.5)):
        if contain % i == 0:
            print(f'{contain} Is not a prime number')
            break
        else:
            print(f'{contain} Is prime number')
while True:
    user_input = input('Enter a number to determine is prime or not or press enter to end: ')
    if user_input == '':
        break
    else:
        num = int(user_input)
        is_prime(num)

#3rd Exercises
list_city = []
count = 0
while count < 5:
    user_input = input('Enter a city name or press enter to end: ')
    if user_input == '':
        break
    else:
        list_city.append(user_input)
        count += 1
for name in list_city:
    print(name)

#4th Exercises
test = [12,4,132,4444]
#Total is : 4592
def sum_int(contain):
    total = 0
    for num in contain:
        total += num
    return total
result = sum_int(test)
print(f'The total in a list: {result}')

#5th Exercises.
test = [1,4,2,3,7,11,12]
def update_list(contain):
    new_list = []
    for num in contain:
        if num % 2 == 0:
            new_list.append(num)
    return sorted(new_list)
def cut_down(contain):
    cut_down = []
    for num in contain:
        if num % 2 != 0:
            cut_down.append(num)
    return sorted(cut_down)
print(f'The original list:{test}')
#[1, 4, 2, 3, 7, 11, 12]
print(f'The cut-down or update list: {update_list(test)}')
#[2, 4, 12]
