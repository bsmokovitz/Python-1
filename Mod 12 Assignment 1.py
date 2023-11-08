Task 1:
#[1]Create a Dictionary that includes all 4 periods(key values) of your school day and what the 4 classes are.
periods = {1: "Econ", 2: "AP CSP", 3: "Python 1", 4: "English 3 Honors"} 
#[2]Print the whole Dictionary
print(periods)
#[3]Pick 1 key value of your choosing and print that.
print(periods[1])


Task 2:
#[1]Use the dictionary below

grocery={“bread”:2.99,”milk”:3.99,”water”:1.19,”cheese”:3.15}

#[2] Add an item and price of your choosing to the dictionary
grocery["chicken"]=5.99
#[3] Use a loop to print the keys with their values on separate lines
for key, value in grocery.items():
    print(key, value)

Task 3:
#[1]Use the dictionary below

ID={57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com']} 

#[2] Create an input statement that as for ID(key)
key = int(input("Enter ID: "))
#[3] Print values of ID selected
print(ID[key])

Task 4:
#[1]Create a dictionary that has 3 items videogame(key), maker, release year, and rating 
videogame = {"name": "Minecraft", "maker": "Mojang", "release year": 2011, "rating": "E"}
#[2] Print only one value of only 1 key
print(videogame["name"])
#[3]Print entire dictionary 
print(videogame)
#[4] Clear dictionary
videogame.clear()
#[5]Print empty dictionary
print(videogame)
