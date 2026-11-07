try:
    # Code that might cause an error
    risky_operation()
except:
    # Code that runs if there's an error
    print("Something went wrong")


#----------------------------------###########-----------------------------

try: 
    result = 10/0 # its a runtime error
except:
    #no matter if you got error on try section except lock will run
    print("Hi there")

#---------------------------------################--------------------------------

try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")