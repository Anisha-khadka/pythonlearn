# # #task
# # # # make a variable and store a data
# # # anisha = 'Hello world'
# # # print(anisha)
# # # anisha1 ="Hello's"
# # # print(anisha1)
# # # anisha2 ='''Hello my name is
# # # "Anusha" khadka'''
# # # print(anisha2)
# # # -----------# List datatype------------
# # a= [1,2,3,'hello',[1,2,3]]
# # print(a)

# # # --------------tuple datatype---------
# # b=(1,2,3,'hello',[],())
# # print(b)

# # # -------set datatype-----
# # c= {1,2,3,'hello',4,"word"}
# # print (c)

# # #------dictionary datatype---
# # {'a':'hello ','b':'world'}

# # # --------Boolean datatype---

# # # ------none type------


# # # operator
# # # 1. Arithmetic operator
# #             # Addition (+)
# # # a= (1,4,8,9)
# # # b=(1,2,3,4,'anisha')
# # # c=a+b
# # # a1=33.4
# # # b1=1
# # # d=a1+b1
# # # print(d)

# # # # d=a-b
# # # print(c)
# # a=10
# # b=5
# # c=a-b
# # print(c)

# # # multiply operator

# # a={'a':'hello'}
# # b=3
# # c=a*b
# # print(c)

# # print the data for 5 times using reusability

# # a=10
# # a +=11
# # print(a)

# # a=44
# # b=33
# # c=11
# # d= a<b or b<c
# # print(d)

# # a=23
# # b=22
# # c=not a>b
# # print(c)

# # a= 4
# # b={4:'hello'}
# # c= a in b
# # print(c)
# # a=5
# # b=4
# # c= a is b
# # print(c)
# a = 23
# y = 22

# a=20
# b=22
# c=23
# if a<b & b<c:
#     print('A')
# elif b>c:
#     print('B')
# else:
#     print('hello')

# a = input("Enter your name:")
# print(a)

# Type conversion
# a = 'hello'
# b = int(a)
# print(b+23)

# Task
# (Exam marks program)
# Ask the user for his/her exam percentage
# Print the status according to the percentage
# If percentage is between 90 to 100 print Outstanding
# If percentage is between 80 to 90 print excellent
# If percentage is between 70 to 80 print very good
# If percentage is between 60 to 70 print good
# If percentage is between 50 to 60 print better
# If percentage is between 40 to 50 print passed
# below 40 failed


# Type conversion
# To int
# a = '23'
# b = 23.4
# c = int(a)
# d = int(b)
# print(c)
# print(d)

# to float
# a = '23.4'
# b = 23
# c= float(a)
# print(c)
# d= float(b)
# print(d)

#  from one group to another

# a = [1, 2, 3, 4] #tuple

# b = tuple(a)  #conversion to set
# print(b)

# a = {'a':'hello'}

# b = str(a)
# print(b)

# loop statement: to make repeated task

# print hello world 10 times
# a = 20
# b = 10
# c=12
# d=10
# while a > b:
#     b += 1
#     print('hello')
#     while c>d:
#         d+=1
#         print('world')

# a = 10
# while True:

#     print('hello world')
#     a -= 1
#     if a == 5:
#         break

a=1
b=5
while b>a:
    a+=1
    if a==2:
        continue
    print('Hello people')
