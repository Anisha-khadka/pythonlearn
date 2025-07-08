# ------------Add to list-----------------------------
# 1. append
epiclist = ["Apple", "Banana", "Mango", "Grapes", "Mango"]
epiclist.append("orange")


# insert
epiclist.insert(2, "Raspberry")
# print(len(epiclist))

# extend
anotherlist = {'a': 'Potato', 'b': 'tomato'}
epiclist.extend(anotherlist)

# ---------Remove from list-----------
# 1. remove()
epiclist.remove('Mango')
# print(epiclist)

# 2. pop()
epiclist.pop(2)
# print(epiclist)

# 3. del()
del epiclist[2]
# print(epiclist)

# del epiclist

# 4. clear()

epiclist.clear()
# print(epiclist)


# Loop through lists
thislist = ["Apple", "Banana", "Mango", "Grapes", "Mango"]

# for i in range(len(thislist)):
#     print(thislist[i])

# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i+=1

# [print (i) for i in thislist]


# list comprehension
# newlist=[]
# for i in thislist:
#     if "a" in i:
#         newlist.append(i)

# print(newlist)

# newlist=[x for x in thislist if "a" in x]
# print(newlist)

# newlist=[x for x in thislist if x!="Apple"]
# print(newlist)
# newlist=[x for x in thislist]
# print(newlist)

newlist = ['hello' for x in thislist]
# print(newlist)

newlists = [x if x != 'Banana' else "orange" for x in thislist]
# print(newlists)


# sorting in list
# *********** ascending ****************
# 1. sort()
# --------alphabetsort-----------
thislist = ["Apple", "Banana", "Mango", "Grapes", "Pineapple", "kiwi"]
thislist.sort()
# print(thislist)

# ----------numerical sort---------
number = [1, 7, 300, 0, 40, 30, 80]
number.sort()
# print(number)


# ***********descending**********************
thislist.sort(reverse=True)  # alphabet
# print(thislist)

number.sort(reverse=True)
# print(number)      #numeric


# *********customize sort function *******

def myfunc(n):
    return abs(n-50)


list = [20, 80, 30, 60, 100]
list.sort(key=myfunc)
# print(list)


# *** case insensitive ********8
thislist.sort(key=str.lower)
# print(thislist)


# ***** reverse order*********

thislist.reverse()
# print(thislist)


# COPY A LIST
# 1. copy()
a = thislist.copy()
# print(a)

# 2. Built-in method list()

# b = list(thislist)
# print(b)

c=thislist[:]
# print(c)

# JOIN LIST
# 1. concat
list1=[1,2,3,4]
list2=[4,5,8,10]
list3=list1 + list2
# print(list3)

# 2. append()
# for x in list2:
#     list1.append(x)
# print(list1)

# for x in list1:
#     list2.append(x)
    
# print(list2)

# 3. extend()
list1.extend(list2)
print(list1)



# SORT LIST
# 1. sort()
# 2. [Reverse=True]
# 3. sort(key=funcname)
# 4. reverse()
# COPY LIST
# 1. copy()
# 2. list()
# 3. slice[:]

#JOIN LIST

# 1. concat
# 2. append
# 3. extend
