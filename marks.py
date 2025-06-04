# Ask the user for his/her exam percentage
# Print the status according to the percentage
# If percentage is between 90 to 100 print Outstanding
# If percentage is between 80 to 90 print excellent
# If percentage is between 70 to 80 print very good
# If percentage is between 60 to 70 print good
# If percentage is between 50 to 60 print better
# If percentage is between 40 to 50 print passed
# below 40 failed

a = input("Enter your percentage:")
b = int(a)

if b >= 90 and b <= 100:
    print('Outstanding')
elif b >= 80 and b < 90:
    print("Excellence")
elif b >= 70 and b < 80:
    print("Very Good")
elif b >= 60 and b < 70:
    print("Good")
elif b >= 50 and b < 60:
    print("Mild")
elif b >= 40 and b < 50:
    print("Passed")
else:
    print("Failed")
