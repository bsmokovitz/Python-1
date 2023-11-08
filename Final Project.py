import datetime
import random 
import os
from time import sleep
import pyfiglet
def clear():
    os.system('cls')
class Character:
    def __init__(self, name, health, height, weight, attacks, attacks_damage, attributes):
        self.name = name
        self.health = health
        self.height = height
        self.weight = weight
        self.attacks = attacks
        self.attacks_damage = attacks_damage
        self.attributes = attributes
    def attack(self, opponent, attacks):
        if opponent.defend():
            print(f"{opponent.name} defended successfully")
        else:
            damage = self.attacks_damage[choice]
            opponent.health -= damage
            print(f"{self.name} used {attacks} and dealt {damage} damage to {opponent.name}")
    def defend(self):
        defense = random.randint(5, 1500)
        self.health += defense
        print(f"{self.name} defended and gained {defense} health")
while True:
    try:
        birth_year = int(input("What year were you born?\n"))
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        if age < 13:
            print("You are not old enough to play this game.")
            exit()
        else:
            print("You are older than 13 years.")
            break
    except(ValueError):
        print("Please enter a valid year.")
print(pyfiglet.figlet_format("Welcome to greak in the city fighter!"))
login= input("Please login or create an account. (login/create) ")
users = []
passwords = []
while True:
    try: 
        if login == "login":
            print("Enter your username: ")
            username = input()
            print("Enter your password: ")
            password = input()
            if username in users and password in passwords:
                print("You have successfully logged in!")
                break
            else:
                print("Invalid username or password.")
        elif login == "create":
            print("Create a username: ")
            username = input()
            print("Create a password: ")
            password = input()
            users.append(username)
            passwords.append(password)
            print("Account created successfully!")
            break
        else:
            print("Please enter a valid command.")
    except(ValueError):
        print("Please enter a valid command.")
zeus = Character("Zeus", 9000, 250, 2.50, ["Thunder Strike", "Lightning Bolt","Thunder Clap"], [500, 800, 1000], ["strength", "agility", "intelligence","durability"])
poseidon = Character("Poseidon", 9000, 220, 2.20, ["earthquake", "tsunami","Ocean's Fury"], [450, 700, 900], ["strength", "agility", "intelligence","durability"])
athena = Character("Athena", 9000, 190, 2.00, ["shield bash", "spear thrust","Owl's Wisdom"], [400, 600, 800], ["strength", "agility", "intelligence","durability"])
ares = Character("Ares", 9000, 230, 2.30, ["war cry", "sword slash","Blinding Rage"], [500, 700, 900], ["strength", "agility", "intelligence","durability"])
hera = Character("Hera", 9000, 210, 2.10, ["healing touch", "curse","Divine Anger"], [400, 600, 800], ["strength", "agility", "intelligence","durability"])
hermes = Character("Hermes", 9000, 200, 2.00, ["blink strike", "teleportation","Sonic Boom"], [450, 700, 900], ["strength", "agility", "intelligence","durability"])
characters = [zeus, poseidon, athena, ares, hera, hermes]
print("Choose your character:")
for i in range(len(characters)):
    print(f"{i+1}) {characters[i].name}")
while True:
    sleep(1)
    clear()
    try:
        choice = int(input()) - 1
        player1 = characters[choice]
        print(f"You chose {player1.name}")
        break
    except(ValueError, TypeError):
        print("Please enter a valid number.")
player2 = random.choice(characters)
while player2 == player1:
    player2 = random.choice(characters)
print(f"Your opponent is {player2.name}")
while player1.health > 0 and player2.health > 0:
    sleep(1)
    clear()
    print("Health Bar:")
    print("Player 1: ", end="")
    for i in range(player1.health//100):
        print("█", end="")
    print()
    print("Player 2: ", end="")
    for i in range(player2.health//100):
        print("█", end="")
    print()
    while True:
        try:
            print(f"{player1.name}'s turn")
            print("Choose an action:")
            for i in range(len(player1.attacks)):
                print(f"{i+1}) {player1.attacks[i]}")
            choice = int(input()) - 1
            if choice < 0 or choice > len(player1.attacks) - 1:
                print("Please enter a valid number.")
            else:
                player1.attack(player2, player1.attacks[choice])
                print(f"{player2.name}'s health: {player2.health}")
                break
            print()
            if player2.health <= 0:
                break
        except(ValueError, TypeError):
            print("Please enter a valid number.")
    try:    
        sleep(1)
        clear()
        print("Health Bar:")
        print("Player 1: ", end="")
        for i in range(player1.health//100):
            print("█", end="")
        print()
        print("Player 2: ", end="")
        for i in range(player2.health//100):
            print("█", end="")
        print()

        print(f"{player2.name}'s turn")
        print("Choose an action:")
        for i in range(len(player2.attacks)):
            print(f"{i+1}) {player2.attacks[i]}")
        choice = random.randint(1, 3) - 1
        player2.attack(player1, player2.attacks[choice])
        print(f"{player1.name}'s health: {player1.health}")
    except(ValueError, TypeError):
        print("Please enter a valid number.")
    print()
if player1.health <= 0:
    print(f"{player2.name} wins!")
else:
    print(f"{player1.name} wins!")

