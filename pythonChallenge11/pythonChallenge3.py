# Using the OOP features inheritance, create a class Animal with the method sound()
# and then create a cat and dog class that inherits from the animal class.
# the cat and dog class should override the sound class and print a different sound
import self as self


class Animal:

    group = "Bird"

    def __init__(self):
        self.sound = "cluck"


class Cat:

    cat_sound = "miu"

    def __int__(self, sound1):
        self.sound1 = sound1


class Dog:

    dog_sound = "woof"

    def __int__(self, sound2):
        self.sound2 = sound2


animal = Animal()
print("Animal:", animal.sound, animal.group)

curl = Cat()
print("\nCat:", curl.cat_sound)

bulldog = Dog()
print("\nDog:", bulldog.dog_sound)

