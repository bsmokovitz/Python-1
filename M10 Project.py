#Task 1

#Create a rock paper scissors game, the game should have:
	#AI that randomly chooses “rock”, “Paper”, Scissors”

	#Input that takes in players choice or Quit(game will continue to run until you type quit)
	#output every time what CPU had and what Player had
	#output whether you won or lost
	#Running count of wins/losses

import random
wins = 0
losses = 0
tie = 0

while True:
    cpu = random.randint(1,3)
    if cpu == 1:
        cpu = "Rock"
    elif cpu == 2:
        cpu = "Paper"
    elif cpu == 3:
        cpu = "Scissors"

    player = input("Rock, Paper, Scissors, or Quit? ")

    if player == "Quit":
        break
        
    elif player == cpu:
        print("Tie!")
        tie += 1
    elif player == "Rock" and cpu == "Scissors":
        print("You win!")
        wins += 1
    elif player == "Rock" and cpu == "Paper":
        print("You lose!")
        losses += 1
    elif player == "Paper" and cpu == "Rock":
        print("You win!")
        wins += 1
    elif player == "Paper" and cpu == "Scissors":
        print("You lose!")
        losses += 1
    elif player == "Scissors" and cpu == "Paper":
        print("You win!")
        wins += 1
    elif player == "Scissors" and cpu == "Rock":
        print("You lose!")
        losses += 1
    else:
        print("Not a choice")

#Task 2

#Create a Christmas, Thanksgiving, New Years Eve Countdown:
	#all Countdowns visible at same time with labels
	#countdowns don’t stop till program is killed by programmer
	#countdowns should show Days,Hours, Minutes, Seconds
	# Thanksgiving: --------   Christmas:------------- New Years:-------------------
	# use console clear to clear screen between loops

import time
import datetime
import os

while True: 
    os.system('clear')
    time.sleep(1)
    now = datetime.datetime.now()
    year = now.year
    chris = datetime.datetime(year, 12, 25)
    thanks = datetime.datetime(year, 11, 28)  
    new = datetime.datetime(year, 12, 31,)

    christmas = chris - now
    thanksgiving = thanks - now
    newyear = new - now
    print("Thanksgiving: " + str(thanksgiving))
    print("Christmas: " + str(christmas))
    print("New Years Eve: " + str(newyear))