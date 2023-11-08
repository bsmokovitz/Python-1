#[1]Create a loop that prints each letter from a user input one letter at a time. 
letter = input("Enter a word: ")
for word in letter:
    print(word)

#[2]From the same input print the word backwards
for word in letter[::-1]:
    print(word)

#[3]From the same input print the word one letter at a time, but every other letter.
for word in letter[::2]:
    print(word)

#[4]Create a program that loops through a word that you get from user input. The loop will capitalize every “i”,”o”, or “u”. You will need an empty string outside the loop to fill with all letters. 
word = input("Enter a word: ")
capitalize=""
for x in word:
    if x == "i" or x == "o" or x == "u":
        capitalize = capitalize + x.upper()
    else:
        capitalize = capitalize + x
    
print(capitalize)


#[5]Write the code for a Mirror Color program. Get user input for favColor. Print favColor backwards and concatenate with favColor. 

#Example:  input Red would give output:  deRRed.

favColor = input("Enter your favorite color: ")
print(favColor[::-1] + favColor)
