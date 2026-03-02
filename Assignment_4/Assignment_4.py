#1st Exercises
def is_valid_course_code(course_code):
    if len(course_code) != 6:
        return False
    if not course_code[:3].upper() or not course_code[:3].isalpha():
        return False
    if not course_code[3:].isdigit():
        return False
    return True
code = input('Enter your course code: ')
print(is_valid_course_code(code))
#2nd Exercises
def color_checking(code):
    color = code.lower()
    cases = '0123456789abcdef'
    if len(code) != 7:
        return False
    if not color.startswith('#'):
        return False
    for char in code[1:]:
        if char not in cases:
            return False
    return True
while True:
    user_input = input('Enter a color code or press enter to end ')
    if user_input == '':
        break
    else:
        print(color_checking(user_input))
#3rd Exercises
def sum_number_in_paragraph(text):
    numbers = []
    current_num = ''
    total = 0
    for word in text:
        if word.isdigit():
            current_num += word
        else:
            if current_num != '':
                numbers.append(int(current_num))
                current_num = ''
    for num in numbers:
        total += num
    return total
sentence = input('Enter a phrase or sentence or press enter to exit: ')
print(sum_number_in_paragraph(sentence))

#4th Exercises
import re
def redact_phone_number(text):
    pattern = r'\+84\d+| \b\d{10}\b'
    return re.sub(pattern,'[REDACTED]', text)
sample = input('Enter a phone number to test: ')
print(redact_phone_number(sample))
    
    
    

