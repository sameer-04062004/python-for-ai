firstName = 'Sameer'
secondName = 'Mughal'

fullName = firstName + ' ' + secondName

dash = '-' * 15

print(fullName)   # print is a built in function
print(dash)

print(len(firstName))
print(len(dash))


name = 'Sameer'
string = f'Hi there, My name is {name}' 

name.lower()
name.upper()

sentence = 'hi, my name is Sameer'
sentence.title()


message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"