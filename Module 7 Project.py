planetname="Jupiter"

#[1]Write the code to access and print the second character from planetName.
print(planetname[1])
#[2] Write the code to access and print the first character from planetName.
print(planetname[0])
#[3]Write the code to access and print the first and last characters from planetName.
print(planetname[0],planetname[-1])
#[4] Write the code to use a negative index to access and print the first character from planetName.
print(planetname[-7])
#[5]Write the code to print planetName sliced from the first 3 characters till the end
print(planetname[0:3])

wiseWords="Play it who opens"

#[6]Write the code to print the first character and then every 3rd character of wiseWords.
print(wiseWords[0],wiseWords[3],wiseWords[6],wiseWords[9],wiseWords[12],wiseWords[15])
#[7]Write the code to print wiseWords in reverse.
print(wiseWords[::-1])

WorkTip="Collaboration and problem solving are important"

#[8] Write the code to find the number of o’s in workTip.
print(WorkTip.count("o"))

codeTip="Good code is commented code"

#[9] Write the code to print a slice of codeTip set start index = 13 and end index = 20.
print(codeTip[13:20])

#[10]Get user input for favFood. Iterate/loop through the letters in favFood and print each letter on a new line
favFood = input("Enter your favourite food: ")
for letter in favFood:
    print(letter)

#[11]Write the code to find and print the length of codeTip
print(len(codeTip))

#[12] Write the code to find and print the midPt (middle) index of codeTip
print(len(codeTip)//2)

#[13] Write the code to search for “code” in codeTip using .find()
print(codeTip.find("code"))

#[14]  Write the code to find and print the number of w’s, o’s and use of the word “code” in codeTip.
print(codeTip.count("w"),codeTip.count("o"),codeTip.count("code"))

#[15]print the code that only prints “Good” and “Code” out of codeTip
good = codeTip.find("Good")
code = codeTip.find("code")
print(codeTip[good:good+4])
print(codeTip[code:code+4])

#[16] Mystery Name program.
#a.       Get user input for firstName.
#b.       Create an empty string variable newName.
#c.       Iterate(loop) backwards through letters in firstName: add each letter to newName as you iterate;
#d.       replace the letter if “e”, “t” or “a” with “?” (hint: use if, elif, elif, else).
#e.       Print newName.   Example Input:  “Alton”	Example Output:  “no?l?”

firstName = input("Enter your first name: ")
name = ""
for letter in firstName[::-1]:
    if letter == "e":
        name += "?"
    elif letter == "t":
        name += "?"
    elif letter == "a":
        name += "?"
    else:
        name += letter
