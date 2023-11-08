#Task 1
#create a list named threeNum with 3 single digit integers
#print threeNum
#check if index 0 is < 5
#if < 5, replace index 0 with the string: “small”
#if > 5, replace index 0 with a string: “large”
#print threeNum
threeNum = [1,2,4]
print(threeNum)
if threeNum[0] < 5:
    threeNum[0] = "small"
elif threeNum[0] > 5:
    threeNum[0] = "large"
print(threeNum)

#Task 2
#create a list threeWords containing 3 different capitalized word strings
#print threeWords
#modify the first item in threeWords to lowercase
#modify the third item in threeWords to swapcase
#print threeWords
threeWords = ["Hello","World","Python"]
print(threeWords)
threeWords[0] = threeWords[0].lower()
threeWords[2] = threeWords[2].swapcase()
print(threeWords)

#Task 3
# insert a name from user input into the partyList in the second position (index 1)
partyList = ["Joana", "Alton", "Tobias"]
#print the updated list
name = input("Enter a name: ")
partyList.insert(1, name)
print(partyList)


#Task 4
 
# Fix the error in the code below
treeList = ["oak"]
print("treeList before =", treeList)
treeList.insert(1,"pine")
print("treeList after =", treeList)
#[what is missing]

#Task 5

#Create a list of 5 names
#write a conditional seeing if the value starts with an “A” (_____.startswith(“A”))
# if the value starts with an “A” replace the value with the word “Apple”
#yes this is a long if statement, if you can figure out how to use a range loop (which I haven’t taught you yet) go for it. 
names = ["Aaron","James","Jake","Hayden","Brayden"]
x = 0
while x < len(names):
    if names[x].startswith("A"):
        names[x] = "Apple"
    x += 1
print(names)


