#lists examples and operations

#creating a list

empty = [] #empty list
numbers = [1, 2, 3, 4, 5] #list of numbers
fruits = ['apple', 'banana', 'orange'] #list of strings
mixed = [1, 'apple', 3.14, True] #list with different data types

print(empty)
print(numbers)
print(fruits)
print(mixed)

text = 'i am kuldeep'
text_list = list(text) #converting string to list
print(text_list)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #list of lists (2D list)
print(matrix)
print(matrix[0]) #accessing first row
print(matrix[1][2]) #accessing element in second row and third column

print(text_list[1]) #indexing in list
print(text_list[-1]) #negative indexing in list
print(text_list[0:5]) #slicing in list
print(text_list[::2]) #slicing with step
print(text_list[1:10:2]) #slicing with start, stop and step
print(text_list[-1:-6:-1]) #slicing with negative step

person = ['kuldeep',24,'ase','bangalore'] 
name, age, profession, city = person #unpacking list into variables
print(name)
print(age)
print(profession)
print(city)

name, *rest , city = person #unpacking list with rest operator (*)
print(name)
print(rest)
print(city)

name, _, profession, _ = person #unpacking list with ignoring some values using underscore (_)
print(name)
print(profession)

numbers = list(range(1, 20)) #creating a list using range function
print(numbers)

print(min(numbers)) #min function to get minimum value in list
print(max(numbers)) #max function to get maximum value in list
print(sum(numbers)) #sum function to get sum of all values in list
print(len(numbers)) #len function to get length of list

number_false = [0, 1, 2, 3, 4, 5] #list with a false value (0)
number_true = [1, 2, 3, 4, 5] #list with all true values
print(any(number_false)) #any function to check if any value is true
print(any(number_true)) #any function to check if any value is true
print(all(number_false)) #all function to check if all values are true
print(all(number_true)) #all function to check if all values are true   

print(numbers.count(1)) #count function to count occurrences of a value in list
print(numbers.index(1)) #index function to find the index of a value in list
