# # binary numbers
# a=bin(4)
# print(a)

# b=int('0b100',2)
# c= int('0b110',2)
# print(c)


# #index
# a="Anisha"
# # start:stop:stepover
# print(a[1:5:2])
# print(a[::-1])
# print(a[::-2])

#built-in function
# greet='hellooo'
# # print(greet[0:len(greet)])
# a=greet.upper()
# b=greet.capitalize()
# c=greet.find('el')
# d=greet.replace('el','ap')

# print(a)
# print(b)
# print(c)
# print(d)

#booleans
# # a=bool(1)
# # print(a)

# #guess the age
# # import datetime
# # birth_year=int(input("Enter you DOB:"))
# # today_date=datetime.date.today()
# # current_year=today_date.year
# # age=current_year-birth_year
# # print(f"you are {age} years old")


# # #password checker
# # username= input("Enter your username:")
# # psw=input("Enter your password:")
# # pswlength=len(psw)
# # pswprivate=pswlength*'*'
# # print(f'Hey {username} , your password {pswprivate} is {pswlength} long')

# #Matrix
# matrix=[[1,2,3],
#         [2,4,6],
#         [7,8,9]]

# print(matrix[0][1])

# sentence=' '.join(['hi','my','name','is','Anisha'])
# print(sentence)

# # list unpacking 
# a,b,*c =[1,2,3,4,5,6]
# print(a)
# print(b)
# print(c)

# dictionary={
#     123:[1,2,3],           #key can be numbers
#     True:'Anisha',         #key can be boolean value
#     a:True             #key cannot be list coz list are mutable/changeable
# }
# #key has to be unique and only use once
# print(dictionary.get('age',44))
# an=dict(name='Anisha')
# print(an)

# user={
#     'name':'Anisha',
#     'age':22,
#     'phone':9080989
# }

# print('age' in user.keys())

# user1=user.copy()    #copy
# print(user.clear())   #clear
# print(user.items())
# print(user1)
# # print(user1.pop('age'))   #pop
# print(user1.popitem())    #popitem
# print(user1.update({'age':55}))     #update
# print(user1)

# set1={1,2,3,4,5}
# sett={1,2,3}
# set2={1,3,5,7,9}
# print(set1.difference(set2))  
# print(set1)                       #difference
# print(set1.discard(5))                   #discard
# print(set1)                     
# print(set1.difference_update(set2))   #difference_update
# print(set1)

# print(set1.intersection(set2))
# print(set1.isdisjoint(set2))
# print(sett.issubset(set1))
# print(set1.issuperset(sett))

# is_old=True
# is_lisenced=False
# if is_old and is_lisenced:
#     print('The old people can drive')
# elif is_lisenced:
#     print('The liscenced and drive')
# else:
#     print('LOLO no')


# Truthy and Falsy ----- values which return true boolean is truthy value
#--- values which return false boolean are falsy
# None, {},0,0.0 etc are falsy values


# Ternary Operator (conditional expression) shorthand
# condtion_if_true if condition else condition_if_else
# is_online=False
# can_message="message allowed" if is_online else "message not allowed"
# print(can_message)

# is_travelling=False
# picture="picture is clicked" if is_travelling else "Picture is not clicked"
# print(picture)


# #short circuiting
# is_friend=True
# is_boy=True

# if is_friend or is_boy:  #its called short circuiting because if
                    #    is_friend is true it doesn't check is_boy to print
    # print("Welcome to the party")
    


# is_magician_input=input("Are you a magician(true/false):").lower().strip()
# is_expert_input=input("Are you an expert(true/false): ").lower().strip()
# is_magician= is_magician_input=='true'
# is_expert =is_expert_input=='true'

# if is_magician and is_expert:   
#     print(is_magician)
#     print("You are a master magician")
# elif is_magician and not is_expert:
#     print("At least you are getting there")
# elif not is_magician:
   
#     print("You need magic powers")
# else:
#     print("invalid syntax")
    
    
# == vs is
# when used ==
# print(True==1)     #True
# print('1'==1)      #False
# print([]==1)       #False
# print(10==10.0)    #True
# print([1,2]==[1,2])      #True

# #when used is
# print(True is 1)     #False
# print('1' is 1)      #False
# print([] is 1)       #False
# print(10 is 10.0)    #False
# print([1,2] is [1,2])      #False

#Dictionary in loops

# user={
#     'name':'Anisha',
#     'age':26,
#     'location':'ktm'
# }

# for i in user:
    # print(i)
# for key,value in user.items():   #both in tuple
    # key,value=i;
    # print(key,value)
    

# for i in user.keys():  #name,age,location
#     print(i)
# for i in user.values():   #Anisha,26,ktm
#     print(i)


#-----counter
my_list=[1,2,3,4,5,6,7,8,9,10]
counter=0
for i in my_list:
    counter=counter+i
    
print(counter)

#-----range: it creates a special type of object that we can iterate
print(range(100))
for num in range(10):
    print('num')
    
for _ in range(5): 
    print('email')
    print(_)
    
for _ in range(2):
    print(list(range(10)))

