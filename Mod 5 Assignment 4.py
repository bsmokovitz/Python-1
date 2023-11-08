#Complete the program using if, elif, else
#Get user input for variable size (S, M, L)
#Reply with each shirt size and price (Small = $ 6, Medium = $ 7, Large = $ 8)
#If the reply is other than S, M, L, give a message for not available
#Optional: Add additional sizes
# [ ] code and test SHIRT SALE program from above instructions

size = input("What size do you want? ")
if size.lower() == "s":
    print("$6")
elif size.lower() == "m":
    print("$7")
elif size.lower() == "l":
    print("$8")
elif size.lower() == "xl":
    print("$8")
else:
    print("We only have, Small, Medium, Large and Xlarge")

#Task 2: Casting with int() & str()
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result
print(int(str_num_1)+int(str_num_2)+int_num_3)

#Task 3 (program): Adding calculator
#Get input of 2 integer numbers
#Print output
#Output Example: 9 + 13 = 22
# [ ] code and test the adding calculator
 
num1 = input("Selcet a number: ")
num2 = input("Selcet another number: ")
print(int(num1)+int(num2))

