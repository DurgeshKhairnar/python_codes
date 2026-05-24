# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class

class Persoe:
    def __init__(Self,name,lastName):
        Self.name = name
        Self.lastName = lastName

    def printName(Self):
        print(f"Name:{Self.name},lastName:{Self.lastName}")

class  Student(Persoe):
    pass

s1 = Student("Durgesh","Khairnar")
s1.printName()       