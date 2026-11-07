age = 22
has_licence = False
# We can save data of multiple types in a list 
my_list = ["Alice", 25, age, True, has_licence]

name = my_list[0]
age = my_list[1]

has_licence = my_list[-1]
second_last = my_list[-2]

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]

# change in list
my_list[0] = "Sameer"

#Now Appending 
my_list.append("Alice") # Add at end

#Now removing
my_list.remove("Alice") #remove by value

my_list.pop() #Remove from end

my_list.insert(1, "Choco") # insert at position (like here at index 1)

del my_list[-1] # remove by index



numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy

