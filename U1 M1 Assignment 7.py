# [] get input for a variable called fav_food, that describes a favorite food
fav_food = input("What is your favorite food? ")
# [] print fav_food as ALL CAPS, used in a sentence
print(fav_food.upper() + " is my favorite food.")
 
# [] print fav_food as all lowercase, used in a sentence
print(fav_food.lower() + " is my favorite food.")
 
# [] print fav_food with swapped case, used in a sentence
print(fav_food.swapcase() + " is my favorite food.")
 
# [] print fav_food with capitalization(title()), used in a sentence
print(fav_food.title() + " is my favorite food.")
 

# Using an “in” Statement to test if “pizza” is in the menu below
 
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print("pizza" in menu)

# Create a menu of three items, create an “in” statement that searches using an input statement to give the variable value.
menu2 = "taco, goldfish, bread"
food = input("What is your favorite food? ")
print(food in menu2)