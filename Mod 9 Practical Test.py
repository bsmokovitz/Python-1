#1.  Get 4 string inputs from the user with the prompts “Enter a noun”, “Enter an adjective”, “Enter a place”, “Enter a second noun”, and “Enter a day of the week”.
#a.  Add the strings into a list called words.
#d.Create a sentence using the variables.
#Example: The [adj] [noun] has been seen at [place] with a [noun2] on [day].
#e.  Print the output
adj = input("Enter a adjective: ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")
noun2 = input("Enter a second noun: ")
day = input("Enter a day of the week: ")
words = [adj, noun,place,noun2,day]
print("The",words[0],words[1],"has been seen at",words[2],"with a",words[3],"on",words[4])

#2. Create a list of 5 animals, call the list “a_list”.  
#Remove the last item and insert it at the beginning of the list. 
#Override the 2nd animal with another one of you choosing
#Run a for loop through the list and print 1 item at a time. 
a_list = ["Dog", "Bird", "Cat", "Mouse","Fish"]
word = a_list[0]
a_list.remove(a_list[0])
a_list.append(word)
a_list.insert(0,"Rat")
for x in a_list:
    print(x)

#3.  Create and print the following list:
#A list of numbers 1-200
list1 = []
for i in range(1, 201):
    list1.append(i)
#A list of numbers 1-50 by 3
list2 = []
for i in range(1, 51, 3):
    list2.append(i)
#A list of numbers 50-10
list3 = []
for i in range(50, 9, -1):
    list3.append(i)
print(list1)
print(list2)
print(list3)

#4. Create a list of 10 food items called food list:
#Sort the list from A-Z
#Print list
#Sort the list Z-A
#Print the List

food_list = ["Fish","Chicken","Apple","Banana","Orange","Taco","Stake","Almonds","Peanuts","Rice"]
food_list.sort()
print(food_list)
food_list.reverse()
print(food_list)

