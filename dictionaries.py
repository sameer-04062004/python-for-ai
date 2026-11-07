person = {
    "Name" : "Alice",
    "age" : 25,
    "city" : "New york"
}

person["age"] # to retrieve value by key

person["Name"] = "Sameer" #to change the value of a key

person["licence"] = True # we can add the new stuff like that

del person["licence"] # we can del stuff like that

if "Name" in person:
    print("Name found")