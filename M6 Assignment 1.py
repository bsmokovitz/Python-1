# Unit 1 Module 4 
# Your Name
# Assignment 1

# [ ] Say "Hello" with nested if
hello = input('Say "Hello" y/n? ')
if hello == "y":
    hello1 = input('Full "Hello"? ')
    if hello1 == "y":
        print("Hello")
    else:
        print("Hi")
else:
    print('"(Friendly nod)"')

# [ ] Create the "Guess the bird" program
bird = ["crow", "hawk", "robbin"]
guess = input("Guess the bird: ")
if guess.lower() in bird:
    print("Yes 1st try!")
else:
    guess1 = input("Guess the bird: ")
    if guess1.lower() in bird:
        print("Yes 2nd try!")
    else:
        guess2 = input("Guess the bird: ")
        if guess2.lower() in bird:
            print("Yes 3rd try!")
        else:
            print("Sorry out of tries")