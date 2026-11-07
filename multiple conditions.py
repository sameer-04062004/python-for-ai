age = 17
has_license = True

weekend = False
holiday = True
raining = False

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")

has_ticket = False

if has_ticket:
    if age >= 18:
        print("Enjoy the movie")
    else:
        print("Needs Supervision")
else:
    print("Please Buy a Ticket")