#Polymorphism


class Animal:
    def speak(self):
        print("I can Roar")

class Human:
    def speak(self):
        print("I can Communicate")

obj = Animal()
obj.speak()

obj1 = Human()
obj1.speak()