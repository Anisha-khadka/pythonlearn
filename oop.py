
# # Iteration 

# mytuple=('apple','banana','mango')
# it=iter(mytuple)
# print(next(it))
# print(next(it))
# print(next(it))

# mystring='Anisha'
# iteration=iter(mystring)

# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))

# for x in mytuple:
#     print(x)
# for x in mystring:
#     print(x)
    
# class Mynumbers:
#     def __iter__(self):
#         self.a=10
#         return self
#     def __next__(self): 
#         if self.a<=20:
#             x=self.a
#             self.a+=1
#             return x  
#         else:
#             raise StopIteration 
# mine=Mynumbers()
# myiter=iter(mine)

# for x in myiter:
#     print(x)
    
    

#OOP Concept

#Inheritance
#Abstraction
#Encapsulation
#Polymorphism


#Inheritance
class Vehicle:
    wheels=4
class Car(Vehicle):
    pass
p=Car()
print(p.wheels)

#Abstraction
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod   #decorator: function which runs before running move method
    def move(self):
        print('This is move class')
        
        
    
# p=Animal()
class Tiger():
    def move(self):
        print('This is move class')
    # pass
p=Tiger()
p.move()

#Polimorphism  #same attribute and method that behave different according to the class
class Animal:
    def move(self):
        print('It is moving')
        
class Dragon:
    def move(self):
        print('It is flying')
        
class Fish:
    def move(self):
        print('It is swimming')
        
animal=Animal()
drag=Dragon()
fish=Fish()

animal.move()
drag.move()
fish.move()

a='Anisha'
b=[1,2,3,4]
c=len(a)
d=len(b)
print(c)
print(d)



    
