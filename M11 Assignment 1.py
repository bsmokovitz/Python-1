#Task 1: Boolean Operators
#Boolean Values (True, False)
# Use relational and/or arithmetic operators with the variables x and y to write:
x = 58
y = 14
#3 expressions (statements that are True) that evaluate to True (i.e. x >= y)
if x >= y:
    print("True")
if x > y:
    print("True")
if x != y:
    print("True")
#3 expressions(statements that are False)  that evaluate to False (i.e. x <= y)
if x <= y:
    print("False")
if x < y:
    print("False")
if x == y:
    print("False")



#Task 2: Combining Comparisons
#Write an expression to test if x is an even number(x%2==0) outside the range [-100, 100]
userinput1 = int(input("Enter a number: "))
if userinput1 % 2 == 0 and userinput1 < -100 or userinput1 > 100:
    print("True")
else:
    print("False")

#Write an expression to test if a string starts with an “S” (.startswith()) and is Ends with a “s”(x[-1])
userinput2 = input("Enter a string: ")
if userinput2.startswith("S") and userinput2.endswith("s"):
    print("True")
else:
    print("False")

         	
#Write an expression to test if a string s contains a numerical value(.isnumeric())
userinput3 = input("Enter a string: ")
if userinput3.isnumeric():
    print("True")
else:
    print("False")


 
#Task 3: Combining Comparisons
#Boolean Expressions Equality
#Write an expression equivalent to the one below to test if x is outside the range [10, 20] 
userinput4 = int(input("Enter a number: "))
if userinput4 < 10 or userinput4 > 20:
    print("In range")
else:
    print("Out of range")


#Task 4: Compound Conditionals
#Write a program to validate that user input is outside the range [0,100]
userinput5 = int(input("Enter a number: "))
if userinput5 < 0 or userinput5 > 100:
    print("In range")
else:
    print("Out of range")


