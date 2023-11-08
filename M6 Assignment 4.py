#Task 1: while with comparison operator
#Program: Animal Names
#Use while to get the user input, animal_name, of 4 animals
#Use a counter, num_animals, in the while loop condition
#Append the names to a string variable, all_animals(outside of loop)
#The loop stops after 5 iterations.
# [ ] Create the Animal Names program, run tests
animals = ""
num_animals = 0
while num_animals < 5:
    animal_name = input("Enter animal name: ")
    animals += animal_name + " "
    num_animals += 1
print(animals)


#Task 2: Using while with a Boolean String
#Program: Long word
#Create a variable named Long Word(blank string outside of loop)
#Create a while loop
#In the loop ask the user for an input for any word
#Have the user input added to Long Word over and over again until you kill the loop by typing “Exit”
# [ ] Create the program, run tests
long_word = ""
while True:
    word = input("Enter a word: ")
    if word == "Exit":
        break
    long_word = long_word + " " + word
print(long_word)


#Task 3: Fix the Errors
#This loop never runs.
#This is a logic error - there is no ErrorMessage, but the code doesn't work
# [ ] review the code, run, fix the Logic error
count = 1
# loop 5 times
while count < 6:
	print(count, "x", count, "=", count*count)
	count +=1
