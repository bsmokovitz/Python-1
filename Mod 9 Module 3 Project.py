#Task 1
#Take in a string input that is more than one word
sentence = input("Enter a sentence: ")
#Turn the string input into a list
words = sentence.split()
#Iterate(loop) through the list:
for i in range(len(words)):
#If there is a word more than 4 characters, make it all uppercase
    if len(words[i]) > 4:
        words[i] = words[i].upper()
#If there is a word less than 4 characters, make it all lowercase
    else:
        words[i] = words[i].lower()
#Sort the list
words.sort()
#Convert the list back to a string using “-” to join the words
sentence = "-".join(words)
#Print the string
print(sentence)


#Task 2
#Take in a string input that is more than one word
string = input("Enter a sentence: ")
#Turn the string into a list
words = string.split()
#pop out the last word and move it to the first word
words.insert(0, words.pop())
#print the list
print(words)

#Task 3
#Take in a number input 
number = input("Enter a number: ")
#split the numbers into a list
numbers = number.split()
#iterate/loop through list add each number together 
total = 0
for i in range(len(numbers)):
    total += int(numbers[i])
#print the total
print(total)

#Task 4
#create 3 list
#list 1 will be all numbers 1-100
list1 = []
for i in range(1, 101):
    list1.append(i)
#list 2 will be all numbers 100-200 by 10s
list2 = []
for i in range(100, 201, 10):
    list2.append(i)
#list 3 will be 80-50 by 3’s
list3 = []
for i in range(80, 49, -3):
    list3.append(i)
#print  all list
print(list1)
print(list2)
print(list3)

