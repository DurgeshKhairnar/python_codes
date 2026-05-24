class Persoe:
    def __init__(Self,name,lastName):
        Self.name = name
        Self.lastName = lastName

    def printName(Self):
        print(f"Name:{Self.name},lastName:{Self.lastName}")

class  Student(Persoe):
    def __init__(Self,name,lastName):
        super().__init__(name,lastName)
        # super().printName()
        Self.name = name
        Self.lastName = lastName


    def printName(Self):
        print(f"last:{Self.lastName},Name:{Self.name}")



s1 = Student("Durgesh","Khairnar")
s1.printName()       