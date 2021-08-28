numbers =[2,2,3,4,4,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(numbers)
print(uniques)