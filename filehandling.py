# File handling

f = open('C:/Users/ACER/Desktop/Python/Text/hello.txt', 'a')
# f.write(' Hello this text was added from a program ')
f.write(' \n 123 ')
# f.write(' \n This is anisha ')
# a = f.read()
# print(a)
f.close()

# write
f = open("hi.txt", 'w')
f.write('Hello')
f.close()

# append
f = open('hi.txt', 'a')
f.write('hi')
f.close()

# read
f = open('hi.txt', 'r')  # rt=readtext  #readline=readsingleline
a = f.read()
print(a)
f.close()

# create ---if exist throws error
f = open('hello1.txt', 'x')
f.write('hi')
f.close()

#delete created file hello1.txt
import os
os.remove('C:/Users/ACER/Desktop/Python/hello1.txt')

#delete folder
os.rmdir('hello')