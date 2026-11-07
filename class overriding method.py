class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"

# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())      # Buddy barks: Woof!
print(cat.make_sound())      # Whiskers meows: Meow!


#--------Adding attributes in child classes----------------
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed      # Dog-specific attribute
    
    def describe(self):
        return f"{self.name} is a {self.breed}"

# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)      # True (inherited from Animal)