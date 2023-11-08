#Q1 Write three (3) print statements that display the 3 types of variables you learned, and what are they used for. 
#example: 
#print(“this is where the answers would go”)
print("Hello Word - This is a String")
print("123 - This is a Intager")
print("1.123 - This is a Float")

#Q2 Write three (3) print statements that display the 3 types of errors with definitions. 
#example: 
print("Type Error is when two different datatypes are being used together")
print("Sentex Error is when you are missing something in the sentax such as quotation marks")
print("Name Error occurs when the funtion name such as print() is incorrect")

#Q3 Write a print statement that displays a number and string together. 
print("This is a string and a number", 123)

#Q4 Create 3 variables called email, school, and grade.  Have the user create values for each variable.  Print the variables in a sentence using string messages. 
email = input("What is your email? - ")
school = input("What is your school? - ")
grade = input("What is your grade? - ")

print("You go to", school, "You are in", grade, "grade and your email is", email)

#Q5 Write a program with a menu with 3 items, then using an in statement print out if one of those items exist in the list or not. 
menu = ["taco", "fish", "apple"]
check = input("Check to see if you can guess what is in the menu? - ")
print(check in menu)

#Q6 Print the string “Hello world” first in all caps and then in a book title using string formatting. 
string="Hello world"
print(string.upper())
print(string.title())

#Q7 Create a program that 1. Asks the user for their street address, then 2. Outputs a string saying “Your street address is:  [their street address.]
address = input("What is your street address? - ")
print("You street address is:", address)

#Q8 Print out your name in surrounded by quotation marks 
print('"My name is Brayden Smokovitz"')

#Q9 Using .isalpha() print True or False of a string of your choosing is only alphabetical. 
print("Hello World".isalpha())

#Q10 Assign 3 variables (2 strings, 1 integer) value, then output them together error free. 
v1= "Taco"
v2= "Fish"
v3= 75
print(v1,v2,v3)
