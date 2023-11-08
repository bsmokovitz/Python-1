#Task 1
 
#Create a list of three currency values named curValues
#Print the list
#Append an item to the list and print the list again
curValues = ['$1','$2','$3']
print(curValues)
curValues.append('$4')
print(curValues)

#Task 2
#define an blank list curNames
#Append additional values to curNames list using input
#Print curNames
curNames = []
curNames.append(input("Enter a name: "))
print(curNames)

#Task 3
#Define an empty list bDaySurvey
#Get user input asking for the day they were born (1-31) or q to finish
#Use a while loop
#Append the b day input to bDaySurvey
#Repeat input until q is entered
#Print bDaySurvey

bDaySurvey = []
bDay = ""
while bDay != "q":
    bDay = input("Enter the day you were born or q: ")
    bDaySurvey.append(bDay)
print(bDaySurvey)


 

