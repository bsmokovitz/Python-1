# [1] Assign your street name (needs to be at least 5 characters) to the variable streetName. Print the 1st, 3rd, and 5th characters.
street = "Colby"
print(street[0])
print(street[2])
print(street[4])

# [2] Create an input variable for a teamName that has “i”, “o” or “u” as the 2nd character.
#  [a]Write the code to test if the 2nd character of the team name is “i”, “o”, or “u”.
# [b]Display the appropriate message stating which letter it contains, and if none of these 3 letters, then display a different appropriate message.
# HINT: you will need to use if, elif and else.
#  Example output:
#  	Team name error, Panthers has 2nd letter “a”.
#  	Good Team name, Cougars has 2nd letter “o”.
teamName = input("Enter a team name: ")
if teamName[1] == "i":
    print("Good team name")
elif teamName[1] == "o":
    print("Good team name")
elif teamName[1] == "u":
    print("Good team name")
else:
    print("Team name error")

#  [3]Assign your street name (at least 5 characters) to streetName. Print the last 3 characters of streetName. 
streetName = "Baker"
print(streetName[-3]+streetName[-2]+streetName[-1])

# [4]Create a variable myName and assign your name to it (at least 5 characters). Print the first and last letter of myName.
myName = "Brayden"
print(myName[0] + myName[-1])
 
# [5]FixIt: Find and fix the errors. Key the code into your program and test it.


shoe = "tennis"
# print the last letter
print(shoe[-1])


