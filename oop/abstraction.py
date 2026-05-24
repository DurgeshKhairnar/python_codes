from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self,name):
        pass


class Dog(Animal):

    def sound(Self,name):
        Self.name = name
        print(f"{Self.name} bark")


s1 = Dog()
s1.sound("Dog")        

