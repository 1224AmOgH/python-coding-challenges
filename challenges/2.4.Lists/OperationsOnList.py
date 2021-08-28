numbers=[2,4,6,8]
numbers.append(20)
numbers.insert(0,10)
num2 = numbers.copy() #copies the list into another variable
numbers.remove(4)
numbers.pop()
print(numbers.count(4)) #Returns the number of times the value appears
print(numbers.index(6))
print(50 in numbers) #in operator is used to check for a sequence of characters
numbers.sort() #Used for sorting the list it sorts in ascending order
numbers.reverse()# reverses the given list
print(numbers)
print(num2)
#clear method is used to clear the list