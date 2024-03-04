#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:

    def __init__(self, name="fido", breed="Beagle"):
        self.name = self.set_name(name)
        self.breed = self.set_breed(breed)

      
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25 :
            return name
        else:
            print("Name must be string between 1 and 25 characters.")


    def set_breed(self, breed):
        if type(breed) == str and breed  in APPROVED_BREEDS:
            return breed
        else:
            print("Breed must be in list of approved breeds.")

fido = Dog(name ="fido", breed="Chihuahua")
print(fido.name)
print(fido.breed)

















