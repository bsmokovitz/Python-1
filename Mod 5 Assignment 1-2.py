#REMEMBER TO CHANGE QUOTATION MARKS WHEN YOU COPY AND PASTE
sunny_today = True
# 1[ ] test if it is sunny_today and give proper responses(“its sunny today” or “its not sunny”) using if and else
if sunny_today:
    print("its sunny today")
else:
    print("its not sunny")


# 2[ ] use if, else to test for islower() for the 2 strings below

test_string_1 = "welcome"
test_string_2 = "I have $3"

if test_string_1.islower():
    print("test_string_1 is all lower case")
else:
    print("test_string_1 is not all lower case")

if test_string_2.islower():
    print("test_string_2 is all lower case")
else:
    print("test_string_2 is not all lower case")

#[3] Using a string you get from an input, create and conditional statement(if/else) to see if the string starts with “w”: (example—if test_string_3.startswith(“w”):);
#print(“word starts with w”) if it does and print(“word doesn’t start with “w”) if it doesn’t

test_string_3 = input("Enter a word: ")

if test_string_3.startswith("w"):
    print("word starts with w")
else:
    print("word doesn't start with w")


X = 9 + 4
# 4[ ] create a test to print(“False) or print(“True”) if X is equal to 13 
if X == 13:
    print("True")
else:
    print("False")

#5[ ] create an if/else statement that tests if y is greater than or equal x + x
# [ ] print output: "y greater than or equal x + x is" ,True/False ((x+x)<y))
x = 3
y = x + 8

if y >= x + x:
    print("y is greater than or equal x + x")
else:
    print("y is not greater than or equal x + x")
