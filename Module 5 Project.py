#Task 1: Use math operators to solve the set of tasks below
# [ ] print the result of subtracting 15 from 43
print(15-43)
# [ ] print the result of multiplying 15 and 43
print(15*43)
# [ ] print the result of dividing 156 by 12
print(156/12)
# [ ] print the result of dividing 21 by 0.5
print(21/0.5)
# [ ] print the result of adding 111 plus 84 and then subtracting 45
print(111+84-45)
# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
print((21+4)*4)

#Task 2: Multiplying calculator function
 
#Get user input() of two strings made of whole numbers
#Get user input() for which operator you want (*,/,+,-)
#Cast the input to int()
#Once all user inputs are taken complete the math

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (*,/,+,-): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Pick one of the following operators (*,/,+,-)? ")

#Task 3: Use math operators to solve the set of tasks below
#Write a program, where you take orders of cheese with the following parameters:

unitPrice = 7.99

#Using input ask user how many units they want:
#Make sure the order is a number (isdigit())
#Make sure the order is above 0 and below 100 (0<int(unit)<100)
#Create a print statement that multiply’s unitPrice times unit. 


units = input("How many units do you want? ")
if units.isdigit():
    if int(units)<1 or int(units)>100:
        print("Pick a number between 1 - 100")
    else:
        print(float(units)*unitPrice)
else:
    print("enter a number")
