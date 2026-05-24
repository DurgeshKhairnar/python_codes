

class student:

    sirName = "Khairnar"

    def __init__(Self,Name): # constructor
        Self.__Name = Name # private variable

    def marks(Self):
        print("My Name is",Self.__Name)


s1 = student("Sai")
s2 = student("Durgesh")
print(s1.sirName)
s1.marks()
s2.marks()