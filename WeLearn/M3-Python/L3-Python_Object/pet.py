class Pet(object):
    def __init__(self, name, age, animal, moves_right, moves_left):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
        self.moves_right = True
        self.moves_left = True
    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"
    def move(self):
        print("> %s is moving to the %s." % (self.name, self.moves_left))


my_pet = Pet("Fido", 3, "Dog", False, True)
print("My pet %s is %s years old" % (my_pet.name, my_pet.age))

# my_pet1 = Pet("Ginger", 6)
# print("My pet %s is %s years old" % (my_pet1.name, my_pet.age))
#
my_pet2 = Pet("rocky" , 1, "Dog" , False, True)
print("My pet %s is %s years old" % (my_pet2.name, my_pet.age))

# my_pet.is.hungry = True
# print("Is my pet hungry? %s" % my_pet.is_hungry)
# my_pet.eat()
# print("How about now?" %s my_pet.is_hungry)
# print("My pet is feeling %s" %s my_pet.mood)

my_pet.moves_left = True
print("I see [my_pet2] has ")
