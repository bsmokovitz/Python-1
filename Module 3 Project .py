# Replace the 3 Comments below with your information:
#Name - Brayden Smokovitz 
#Date - 9/12/2022
#Class - Python Programming I

#[ ] Get user input for 5 friends and save in variable: FriendsTest.
#Ex.
#Friend1=input(“Enter a Friend1”)
#Friend2=input(“Enter a Friend2”)
FriendsTest1 = input("Enter a Friend")
FriendsTest2 = input("Enter a Friend")
FriendsTest3 = input("Enter a Friend")
FriendsTest4 = input("Enter a Friend")
FriendsTest5 = input("Enter a Friend")

#[ ]print out all the friends entered on one line
print(FriendsTest1, FriendsTest2, FriendsTest3, FriendsTest4, FriendsTest5)

#[ ]create a variable that contains all the friends, name the variable “FriendsTest”
#FriendsTest=Friend1 + Friend2......
FriendsTest = FriendsTest1 + FriendsTest2 + FriendsTest3 + FriendsTest4 + FriendsTest5

#[ ]Print a literal string statement for Friend1(ex.”One of my Friends is named”,Friend1”)
print("One of my Friends is named", FriendsTest1)

#[  ]Print an in Statement to show if “Jane” is in FriendsTest.
print("Jane" in FriendsTest)


#[ ]Create a print statement that uses all the friends in a sentence of you choosing. 
print("One of my Friends is named", FriendsTest)

#[ ]Create an input statement assigned to the variable check.
#Test if check is in FriendsTest.
#(use “in” Statements for each.)
check = input("Enter a name")
print(check in FriendsTest)