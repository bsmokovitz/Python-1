#Task 1: Containment (in, not in)

numberlist = [22, 89, 69, 78, 58, 22, 56, 13, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38, 25, 96]
#[1]Write a program that asks a user if the number they entered is in the list below.  (use a for loop if you want just need an in statements)
num = input("Enter a number: ")
if int(num) in numberlist:
    print("Number is in list")
else:
    print("Number is not in list")

#[2]Run test to see if “applicant” is in “records”

records = [['Colette', 22347], ['Skye', 35803], ['Alton', 45825], ['Jin', 24213]]
applicant = ['Joana', 20294]

if applicant in records:
    print("The applicant is in the records")

#Task 2: 

#Write a program that makes a basic “is” statement.  Assign Numbers to a different variable and use “is” in a print statement to see if the variable has been reassigned.

Numbers=[5,3,2,6,8,45,3,2,3,5,78,2,34,0]
Numbers2=Numbers
print(Numbers is Numbers2)

#Task 3: 
#Correct the following expression so the answer is `True`
print(6 + 2 < 9)

#Correct the following expression so the answer is `True`

print(3 ** 2 + 1 <= 3 * 8 + 1)

#Correct the following expression so the answer is `True`

print(4 + 3 * 2 <= 16)

#Correct the following expression so the answer is `True`

print(4 > 3 and 5 + 6 > 7)


#Task 4: Tuples
#[ ] Write a program to merge the two sorted tuples T1, T2 into a larger (also sorted) tuple T3
 
# Output should be:
#Merged sorted tuple:
#(12, 13, 15, 20, 20, 26, 30, 37, 40, 55, 60, 68, 72, 78, 81, 84, 89, 97, 97, 18 0)

# sorted tuples
T1 = (15, 20, 30, 37, 55, 60, 78, 81, 84, 100)
T2 = (12, 13, 20, 26, 40, 68, 72, 89, 97, 97)
T3 = list(T1) + list(T2)
T3.sort()
print(tuple(T3))

 
#Task 5: Tuples cont.
T = (257, 462, 18, 369, 415, 994, 541, 752, 78, 895, 0, 576, 40, 552, 438, 605, 54, 296, 433, 986, 685, 651, 523, 855, 777, 437, 65, 360, 265, 858, 260, 819, 586, 358, 860, 250, 531, 7, 801, 259, 155, 376, 374, 828, 475, 62, 52, 184, 186, 283, 643, 86, 472, 267, 692, 750, 948, 683, 452, 770, 322, 492, 871, 360, 88, 883, 764, 288, 383, 411, 679, 90, 857, 802, 974, 403, 798, 990, 475, 260, 289, 438, 873, 779, 895, 939, 462, 469, 183, 520, 366, 267, 896, 732, 303, 754, 195, 949, 546, 180)
# [ ] Complete the function `simple_stats` so it returns:
# 1) The maximum number in the tuple T
# 2) The minimum number in the tuple T
# 3) The average of the numbers in the tuple T

def simple_stats(T):
    max_num = max(T)
    min_num = min(T)
    avg_num = sum(T)/len(T)
    return max_num, min_num, avg_num
 
 
#have outputs(prints) that show the largest, smallest and average numbers
print(simple_stats(T))
 