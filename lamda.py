# x=lambda a:a +10
# print(x(5))

# y=lambda a,b:a*b
# print(y(5,6))


# #scope

# def myfunc():
#     x=100
#     def myfunc2():
#         print(x)
#     myfunc2()
    
# myfunc()

# import mymodule

# mymodule.greetanisha('Anisha')

# import moduletest

# moduletest.propose("Anisha")

# import platform
# x=platform.system()
# print(x)

# y=dir(platform)
# print(y)
# from mymodule import greetanisha

# import datetime

# z=datetime.datetime.now()
# print(z.year)
# print(z.strftime('%A'))

#Built-in math function
# 1.....min,max 
# p=(2,6,0,10,7,-3)
# x=min(p)
# y=max(p)
# print(x)
# print(y)


# 2.... absolute(positive)
# z=abs(-10.4)
# print(z)

# 3... power
# l=pow(2,3)
# print(l)

# built-in  math module
# a......math.sqrt()
# import math
# p= math.sqrt(4)
# print(p)

#b...math.ceil() and math.floor()
# x=math.ceil(2.44)
# y=math.floor(3.33)
# print(x)
# print(y)

# #c.... math.pi
# x=math.pi
# print(x)


import json

dict={
    'name':'Anisha',
    'age':22
}
x=json.dumps(dict,indent=2,separators=("." ,"="),sort_keys=True)
print(x)
