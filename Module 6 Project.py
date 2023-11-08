#Unit 1, Module 4, Project 1—------(ALL TO BE DONE ON SAME FILE)

#[1]   Write a program that shows all numbers between 1 and 100 instantly.
x = 0
while x < 100:
    x += 1
    print(x)

#[2]  Write a program that asks the user to pick a color you choose. 
#Have the program keep track of the number of guesses it takes for the user to get it right.
#The program will stop when the User guesses the right color
color = "blue"
tries = 0
while True:
    guess = input("Guess a color? ").lower()
    if guess == color:
        tries+=1
        print("Correct! It took you",tries,"tries!")
        break
    else:
        tries+=1
        pass

#[3]  Write a program that collects string input (words) until the user enters
#STOP. Combine the strings into a sentence.Basically add a bunch of words together until
#you type stop
words = ""
while True:
    word = input("Enter a word: ")
    if word == "stop":
        print(words)
        break
    else:
        words = words + " " + word
        pass



#[U1M4 Project 2—--------------------------------
#I would like you to re-create a guess it game with the following criteria this time with a loop
#1.       Set a variable called correct_number equal to whatever number you choose(a number between 1-50)
#2.       Have an input variable called guess
#3.       Make sure the input is a digit otherwise ask for a num
#4.       Your program will loop until guess==correct_number
#5.       If the guess is to high print “Your guess is too high, guess again”, if you guess is too low print “Your guess is too low”, the it asks again, until you guess It correctly
#6.       You will have a count every time your program loops to keep track of how many guesses you too.
#7.       When the user gets it right print “You got it right, it took you ___ Tries”  the blank will be filled with your count variable.  

correct_number = 5
while True:
    num = int(input("Enter a number: "))
    if num == correct_number:
        print("Correct!")
        break
    elif num > correct_number:
        print("Too high!")
        pass
    else:
        print("Too low!")
        pass

#Challenge Assignments(optional)—--------------------------------------

#[1]  [Challenge]: Write a program that asks the user five questions. Have at least three of
#the questions ask follow-up questions based on the user’s answer. Display all
#the results to the user.

#[2]  [Challenge]: Write a gradebook program that allows a user to enter 5 grades at the end of
#The program should then print out the average of all grades
#all inputs needs to be numbers

#[3]  Write a program that adds all even numbers between 1 and 50. 
#You will need:  if x%2==0 to filter even numbers:
