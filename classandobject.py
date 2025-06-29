class myclass:
    pass

# a = myclass()
# print(a.x)


class Person:
    def __init__(mysillyparameter, age, name):  # init is built-in function
        mysillyparameter.age = age
        mysillyparameter.name = name

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("This is mine"+self.name)


p = Person(22, "Anisha")
# del p
# del p.age
print(p.age)
print(p.name)
# p.age=33
p.name = "Parvati"

print(p)
p.myfunc()


class Car:
    name = 'honda'
    price = 40000
    max_speed = '300km/hr'

    def get_max_speed(self):
        print(self.name)

    def set_max_speed(self, newmaxspeed):
        self.max_speed = newmaxspeed
        self.get_max_speed()


p = Car()
# p2=Car()
# p.name="Farari"
p.color = "Black"
# print(p.color)
# print(p.name)
# print(p2.name)
# print(p.price)
# print(p.max_speed)
# p.get_max_speed()
p.set_max_speed('400km/hr')

a = 'Anisha Khadka'.upper()
print(a)


# Requirements
# Make a cow class which should have attributes to  define cow object and methods like : move, eat, get_legs,get_ears
# Make a object of cow  class and interact with the methods and attributes

class Cow:
    move = 'running'
    eat = 'grass'

    def get_legs(self):
        print(self.move)
        # print("Cow is running")

    def get_ears(self, newmove):
        self.move = newmove
        self.get_legs()

        # print("Cow has two ears")


features = Cow()
print(features.move)
print(features.eat)
# features.get_legs()
features.get_ears('walking')


# Magic method

# class Gossipgirl:
#     maincharacter = 'Blair Waldorf'
#     age = '22'
#     boyfriend = 'Nate Archibal'
#     formerpartner = 'Chuck Bass'

#     def gettogether():
#         print('Anisha')
#     def __init__(self):
#         print('Hello')
        
class Gossipgirl:

    def __init__(self,maincharacter,age,boyfriend,formerpartner):
        self.mainc=maincharacter
        self.age=age
        self.boy=boyfriend
        self.fp=formerpartner
    def gettogether(self):
        print(self.fp)

p = Gossipgirl('Blair Waldorf',22,'Nate Archibal','Chuck Bass')
p.gettogether()
print(p.__dir__())

# a=23
# b=34
# c=a.__add__(b)
# print(c)


