#Its a simple function 
def add_print(a,b):
    print(a + b)
#its just printing the output not storing that we can use later
# It just up in terminal when we run
add_print(a=7,b=8)

res = add_print(a=7, b=8)
print(res) #output = None # becouse we just print the value show it and it cant store anywhwere

#------------------------------------------------------------------------------

def add_return(a,b):
    return a + b
# Its returning and we capture it and we can store it as information for using later
# It don't show up in terminal it returns value that can store and use later
add_return(a=4, b=5)

#like we can save it in result and use that result variable further
result = add_return(a=4, b=8)

print(result) # output = 12  #look it will show output that is stored by return

#------------------------------------------------------------------------------------

def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

#----------------------------------------------------------------------------------------

def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")

#----------------------------------------------------------------------------------------

def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_no = numbers[0]
    last_no = numbers[-1]
    return first_no, last_no

first, last = simple_function()

#------------------------------------------------------------------------------------

def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!