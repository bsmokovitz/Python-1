#1 Create a program that has a user input that guesses a number you already have chosen. If the user guesses correctly then it will say, “You got it right!”.  If the user guesses higher than the number then it will say, “You guessed too high.” If the user guesses lower than the number then it will say, “You guessed too low.”
num = 28
guessNum = int(input("Guess a number: "))
if guessNum == num:
    print("You got it right!")
elif guessNum > num:
    print("You guessed too high.")
else:
    print("You guessed too low.")

#2 Create a program that has two inputs, one asking, “What flavor of ice cream do you want?”, the other one saying “How many scoops do you want?”
#-          Print the following given the inputs
#o   Chocolate
  #“Chocolate is my favorite too. You are getting [number] scoops.”
#o   Strawberry
  #“You are getting [number] scoops of Strawberry. Sweet!”
#o   Vanilla
  #“Vanilla is awesome! You are getting [number] scoops.”
#o   Else
  #“We don’t have that flavor.”

flavor = input("What flavor of ice cream do you want? ")
scoops = input("How many scoops do you want? ")
if flavor.lower() == "chocolate":
    print("Chocolate is my favorite too. You are getting " + scoops + " scoops.")
elif flavor.lower() == "strawberry":
    print("You are getting " + scoops + " scoops of Strawberry. Sweet!")
elif flavor.lower() == "vanilla":
    print("Vanilla is awesome! You are getting " + scoops + " scoops.")
else:
    print("We don’t have that flavor.")



