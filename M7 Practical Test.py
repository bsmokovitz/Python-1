
#You are sending information back and forth with a friend and you don’t want anyone else reading your data. To prevent others from knowing the content of your notes, you decided to create a mystery code.
#--Get user input for inputWord
#-- make sure input accounts for upper and lower case being entered
#--Assign newWord to an empty string
#-- Iterate/loop through letters in inputWord backwards.  Add each letter to newWord as you iterate
#-- Replace the letter if “a” with “@”,  “e” with “#”, “i” with “%”, and “o” with “*”, and pick 4 other letters that you change for something else.(hint: use if, elif, else)
#---Once completed, print newWord one letter at a time.(You will need a completely different loop)
#Hint: be sure to test your program multiple times using each of the letters.
 
inputWord = input("Enter a password: ")
newWord = ""
for i in inputWord[::-1]:
    if i == "e":
        newWord += "?"
    elif i == "t":
        newWord += "?"
    elif i == "a":
        newWord += "?"
    else:
        newWord += i

for i in newWord:
    print(i)
    

