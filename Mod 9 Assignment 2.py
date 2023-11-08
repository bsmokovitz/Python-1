#Task 1 range(stop)
#, use range(x) to print the numbers 1 through 5,
for i in range(1,6):
    print(i)



# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
#total*=x
# Initialize total as 1 not 0!
total=1
for i in range(1,8):
    total*=i
print(total)

#Use loop slicing to print the second half of spellList below # [ ] print the second half of a spelling list using a range(stop) loop to iterate the list
spellList = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]
for i in range(4,7):
    print(spellList[i])

#Task 2 range(start,stop)
fiveFifteen=[ ]

# [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: fiveFifteen
# [ ] print list fiveFifteen
for i in range(5,16):
    fiveFifteen.append(i)
print(fiveFifteen)


# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spellList
# output should include "February", "November", "Annual"

spellList = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for i in range(2,5):
    print(spellList[i])


#Task 3 range(start,stop,step)
 
# [ ] print numbers 10 to 20 by 2's using range

for i in range(10,21,2):
    print(i)


# [ ] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20
for i in range(20,9,-1):
    print(i)
 
#Task 4: fix the error
# [ ] fix the error printing odd numbers 1 - 9
for num in range(1,10,2):
    print(num)

