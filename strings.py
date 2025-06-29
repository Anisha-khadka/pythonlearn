# #----strings-----------------
# #definition: strings are array of bytes representing unicode characters

# # 1>>>>>>>> About string basics
# # looping through strings
# a="Anisha"
# for i in "Apple":
#     print(i)
# #string length
# print(len(a))

# #check string (identity operator)
# text="This is my text and i love it"
# if "love" in text:
#     print("Yes, there is 'love' in the text")

# if "loves" not in text:
#     print("No, there is no 'loves' in the text")


# # 2>>>>>>>>> Slicing strings

# txt="Anisha Khadka"
# print(txt[1:5])
# print(txt[:5])
# print(txt[-5:-1])
# print(txt[-5:])



# # 3>>>>>>>> Modify string

# my_text = " This is my lovely text "
# # uppercase
# print(my_text.upper())

# # lowercase
# print(my_text.lower())

# # remove whitespaces from start and end of text
# print(my_text.strip())

# #replace string
# print(my_text.replace("my","our"))

# #split string  returns a list specified seperator becomes list
# print(my_text.split(","))


# # 4>>>>>>>>>>>>Format Strings F-strings
# age=33.444333
# age1=20
# print(f"Hello you are {age:.3f} years old")
# print(f"Hello you are {age1*2} years old")
# x=9
# print(f"The price is {x:.2f} dollars")

# # 5>>>>>>>>Escape Character \
# this_is_a_text="We are in a vacation in \"Bali\" "
# print(this_is_a_text)
# #other examples:
# a= "I love \\"
# print(a)

# 5>>>>>>>>>>>>>> String methods
s="this is the sentence"

# a. capitalize (converts the first char to uppercase)
print(s.capitalize())

# b. casefold (converts string to lowercase)
print(s.casefold())

# c. center (returns a centered string)
print(s.center(60,"*"))

# d. count(returns a num of times a value occurs in string)
print(s.count('t'))

# e. encode(returns the encoded version of string)
print(s.encode()) 

#boolean


# class myclass():
#     def __len__(self):
#         return 0
# obj=myclass()
# print(bool(obj))

# x=200
# print(isinstance(x,float))