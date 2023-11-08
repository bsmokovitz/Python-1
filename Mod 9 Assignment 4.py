#Task 1: Using . split()
# [ ] split the string(rhyme) into a list of words (rhymeWords)
# [ ] print each word on it's own line

rhyme = 'Jack and Jill went up the hill To fetch a pail of water'
split = rhyme.split()
for x in split:
    print(x)

# [ ] split codeTip into a list and print the first and every other word

codeTip = "Python uses spaces for indentation"
split = codeTip.split()
print(split[::2])


#Task 2 .split()
# [ ] split poem into a list of phrases by splitting on "*" a
# [ ] print each phrase on a new line in title case                	
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
split = poem.split("*")
for x in split:
    print(x.title())


#Task 3 .join()

# [ ] .join() letters list objects with an Asterisk: "*"

letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
print("*".join(letters))
#Task 4 Program: Choose the separator
#Create a program that get user input on what to use to join words (" ", *, -, etc...) - store in variable: separator join pharseWords with the separator and print

# [ ] complete Choose the separator
phraseWords = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
userInput = input("What would you like to use to join the words? ")
print(userInput.join(phraseWords))

#Task 5
print('The String', end='-')
print('The String', end='-')
print('The String', end='-')
# [ ] use 3 print() statements to output text to one line
# [ ] separate the lines by using "- " (dash space)



#Task 6

Msg_characters = list("Always test your code")
 
# [ ] create a string (fact) of 20 or more characters and cast to a list (factLetters)
# [ ] print the new list

fact = "This is a string that will have 20 or more charaacters. I don't feel like counting them though. So im just going to keep typing untill i believe it has 20 or more characters. I think this is good enough."
factLetters = list(fact)
print(factLetters)

