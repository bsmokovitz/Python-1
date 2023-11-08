#Task 1: while True
#[ ] Program: Get a name forever ...or until done
#use while True:
#ask for user input for name 
#keep asking until name starts with a “h”
#break loop and print a “hello” + name
# [ ] create Get Name program

while True:
    name = input("Enter a name: ")
    if name.startswith( "h") or name.startswith( "H"):
        print("Hello "+name)
        break
    else:
        pass

#Task 2: Incrementing in a while() loop
#Program: Shirt Count
#Enter a sizes (S, M, L)
#Tally the count of each size
#Input "exit" when finished
#Report out the purchase of each shirt size
# [ ] Create the Shirt Count program, run tests

s = 0
m = 0
l = 0

while True:
    size = input("Enter a size: ")
    if size == "s":
        s+=1
        print(s,"SCount\n",m,"M Count\n",l, "L Count")
    elif size == "m":
        m+=1
        print(s,"Count\n",m,"Count\n",l,"Count")
    elif size == "l":
        l+=1
        print(s,"Count\n",m,"Count\n",l,"Count")
    elif size == "exit":
        break
    else:
        pass
