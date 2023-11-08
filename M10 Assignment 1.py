#TASK 1: Importing Modules

#  Import math
import math
 
#  Write 2 input statements assigning a variable to a user input to enter an integer for each   	input 
#hint: use int()
x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))

#  Find the gcd of the two integers 
print(math.gcd(x, y))

#TASK 2: Using math Functions
 #iterate through numlist print square root (sqrt()) of all even numbers pass on odds.
# if (num%2==0):  if x was your loop variable will show even numbers
numList = [25, 34, 193, 2, 81, 26, 44]
for num in numList:
    if (num%2==0):
        print(math.sqrt(num))


#TASK 3: Operator Precedence
 # Correct the following expression so the answer is 10
print(2 + 16  / 2)
 
# Correct the following expression so the answer is 125
print(42 + 3 ** 4)
 

#TASK 4: Rounding Numbers
 
# Use an appropriate rounding functions to round 75.34 to 75 and then to 76:
x = 75.34
print(round(x))
# Hint: Use trunc, floor, ceil to round up and down
# Use an appropriate rounding function to fix the following ‘float’ error
# Price of a chocolate box

p = 4.35
print(math.floor(p))
p = math.floor(p)

# Quantity needed

q = 200

# Order total price (Should be 4.35 * 200 = $870.00)

total = p * q

print("Total price: ", total)

#Task 5: Generating Random Integers
#import random
import random
#create a dice roll with random int 
print(random.randint(1,6))
 

#TASK 6: Random Sequences
card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']	
#using choice or shuffle, produce a random card from the lists above.
print(random.choice(card_type))
 
#  Print the randomly picked card
print(random.choice(card_number))
 
#The following list contain the 10 most populous American cities; write code to randomly select one of the cities to visit

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

#  Import choice from random
from random import choice
 
#  Create a variable that will become your random city
city = choice(cities)
 
#  Print randomcity
print(city)

