# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

class Student:

    __sirName = "Khairnar"
    def __init__(Self,Name):
        Self.__Name = Name  # private variable

    def getName(Self):
            return Self.__Name
        
    def setName(Self,Name):
            Self.__Name = Name

      # private method
    def __show(self):
        print("Name:", self.__Name)

    # public method
    def display(self):
        self.__show()
        


s1 = Student("Durgesh")
print(s1.getName())
s1.setName("Sai")
print(s1.getName()) 
print("---displayMethod----")
s1.display()           