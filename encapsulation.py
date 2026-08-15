#Encapsulation

class Animal:
    _name = "Lion"
    __age = 12


obj = Animal()
print(obj._name)                        #Protected Encapsulation
print(obj.__age)                        #Private Encapsulation