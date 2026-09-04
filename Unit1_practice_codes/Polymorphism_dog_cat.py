class Dog:
    def speak(self):
         return "woof woof !"

class Cat:
     def speak(self):
          return "moew moewww...!"

#Polymorphic interface via duck typing
def animal(entity):
     print(entity.speak())

animal(Dog())
animal(Cat())
