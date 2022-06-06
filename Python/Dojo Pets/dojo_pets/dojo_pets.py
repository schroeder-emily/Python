from configparser import NoSectionError


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 200
        self.energy = 100
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        self.energy -= 10
        return self
    def noise(self):
        print(self.noise)
        return self


tricks = ["Sleeping", "Barking at birds", "Beating up little sis"]
noise = ["Meow"]

ducky = Pet("Ducky", "Cat", tricks)


treats = ["Tuna", "Deli Meat", "Ice Cream"]
pet_food = ["Natural Balance", "Wellness"]    

emily = Ninja("Emily", "Schroeder", treats, pet_food, ducky)    

emily.feed().walk().bathe()
print(emily.first_name)
print(emily.treats[0])
print(ducky.energy)
print(ducky.name)
print(ducky.type)

ducky.eat()
print(ducky.energy)

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def sleep(self):
        self.energy += 30
        return self
    def eat(self):
        self.energy += 10
        self.health += 20
        return self
    def play(self):
        self.health += 15
        self.energy -= 20
        return self

tricks = ["Fetching", "Cuddling", "Sitting"]
moose = Dog("Moose", "Dog", tricks)

moose.eat().play().sleep()
print(moose.energy)
print(moose.type)
print(moose.name)
print(moose.tricks[0])
