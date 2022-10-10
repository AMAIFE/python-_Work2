
#Function Task 10

def greetings():
    print("Hello World")


def status():
    pass


greetings()
status()


#Annonymous Function Task 10


hello = lambda : print("Hello World")
hello()


#Assignment 11

def add(num1=3, num2=3):
    result = num1 + num2
    print("Result", result)


def description(course):
    print("Course", course)


description("Testify Python")
add()


#Assignment 12

language = "python"


def name():
    language = "java"
    print("language", language)


print(language)
name()


#Assignment 13

def print_hello():
    print("hello world")
    print_hello()


print_hello()

#Assignment 14

name = "excellence"
upper = name.upper()
print("upper", upper)


#Assignment 15

food_type = ["salad", "potatoes", "beans", "22", "44"]
print("food", food_type)

#remove an item from the list
food_type.remove("beans")
print("remove", food_type)

#insert an item in the list using append
food_type.append("plantain")
print("append", food_type)


#Assignment 16
Country = {
    "nigeria": "delta",
    "usa": "north carolina",
    "liberia": "bomi"
}
print("dictionary:", Country)

#add more keys value
Country.update({"colour": "yellow,blue"})
Country.update({"sizes": "large,medium"})
print("dictionary update:", Country)
