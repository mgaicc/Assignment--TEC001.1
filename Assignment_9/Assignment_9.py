#1st Exercise
def count_line(filename):
    count = 0
    with open(f'{filename}.txt','r') as file:
        for line in file:
            if line.strip() !='':
                count += 1
    return count
result = count_line('mbox-short')
# print(result)
#2nd Exercise
def specific_character(fliname,keyword):
    with open(f'{fliname}.txt','r') as file:
        contain = []
        for line in file:
            for index,line in enumerate(file,start=1):
                if keyword in line:
                    contain.append(index)
        return contain
result = specific_character('mbox-short','Sat')
print(result)
#3rd Exercise
def uppercase(filename):
    with open(f'{filename}.txt','r') as file:
        content = file.read()
    with open('output.txt','w') as outfile:
        outfile.write(content.upper())
result = uppercase('mbox-short')
#4th Exercise
def average(filename):
    count = 0
    total = 0
    with open(f'{filename}.txt','r') as file:
        for line in file:
            if line.strip() == '':
                continue
            name,score = line.split(',')
            total += float(score)
            count += 1
    return total / count
result = average('Input_value')
print(result)

        
            