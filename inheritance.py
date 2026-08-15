class Animal:                             #Parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age



class Human(Animal):                       #Child class
    def __init__(self, name, age,hobby):
        super().__init__(name, age)
        self.hobby = hobby


obj = Animal("Lion",12)
obj1 = Human("Vedant",32,"Swimming")

