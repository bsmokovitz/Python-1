msg = "Hello"
# [1 ] print the True/False results of testing if msg string equals "Hello" string
if msg == "Hello":
    print(True)

# [2 ] get input for a variable, answer, and ask the  user 'What is 8 + 13? : '
#  print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string" make sure you use int()
answer = input("What is 8 + 13? : ")
if int(answer) == 21:
    print("Correct")
else:
    print("Incorrect")
 
# [ 3] Create the program  that takes an input of any True/False question and if the user is correct prints “You are the winner” if incorrect print(“you are a loser”)
question = input("Do you have two eyes?: ")
if question.lower() == "true":
    print("You are the winner")
else:
    print("You are a loser")


#[4] Create a program takes in two integers(don’t forget to cast), if the total is more than 30 print(“The number is higher than 30”) if lower print(“the number is lower than 30”)
num1 = input("Enter a number?: ")
num2 = input("Enter another number?: ")
if int(num1) + int(num2) > 30:
    print("The number is higher than 30")
else:
    print("The number is lower than 30")
