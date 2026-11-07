def greet_alice():
    print("hello Alice!")

greet_alice()

def greet(name):
    print(f"hello {name}")

greet("Sameer")

greet(name="SAMEER")

def greet1(firstname, lastname):
    print(f"Hello {firstname} {lastname}")

greet1(firstname="Sameer", lastname="Akram")

greet1("Sameer") # It will give now error because function is accepting two parameters

def greet2(lastname, firstname="Sameer"): #if we use predifined parameter we have to putit on last otherwise it will give error
    print(f"Hello {firstname} {lastname}")

greet2(lastname="Akram")

greet2(firstname="Ali", lastname="Akram") # we can also change the predefined parameter at run time

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98, iT wrls but good to use keyword argument

calculate_total(price=100, tax_rate=0.08, discount=10) # using keyword argument

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)