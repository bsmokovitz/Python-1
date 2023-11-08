from datetime import time, date, datetime
#Task 1: time Objects
#[1]Create a ‘time’ variable called T1 containing the time: 8:45 AM
T1 = time(8,45)
#Print T1
print(T1)
#.[2]Create a ‘time’ variable called T2 containing the time 8:45:01:000150 PM
T2 = time(20,45,1,150)
#Print T2
print(T2)

#[3]Modify t3 to 4:10 PM given:
t3 = time(hour = 4, minute = 10, second =0) 
#print t3
print(t3)


#Task 2: date Objects
#[1]Create a ‘date variable D1 containing: (March 28 2012)
D1 = date(2012,3,28)
#Print D1
print(D1)
#[2]Prompt the user to enter a month and day, get the current year, then create a date object with the information collected
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
#Get the current year
year = date.today().year
#Create variable currentDate =and get today’s date
currentDate = date(year,month,day)
#Create variable y and assign currentDate.year
y = currentDate.year
#Create a new date object
newDate = date(y,month,day)
#Create the variable d and assign attributes for date such as month = m etc.
d = newDate.strftime("%B %d %Y")
#Print d (it will be the combination of user month,day given and the year you found)
print(d)


#Task 3: datetime Objects
#[1]Create a “datetime” variable DT1 containing: March 28 2012 @ 12:55:10:30 AM
DT1 = datetime(2012,3,28,12,55,10,30)
#Print tDT1
print(DT1)
#[2]Write the code that prints the current hour
print(datetime.now().hour)
#Create variable named dt and slice today from datetime
dt = datetime.today()
#Print the current hour
print(dt.hour)
#[3]Write a program that prints the current date on one line and the current time on another line
print(datetime.now().date())
#Create the variable dt and assign datetime and slice for today
dt = datetime.today()
#Create a variable for time and date and split time and date from dt
time = dt.time()
#Print the current date
print(dt.date())
#Print the current time
print(time)

import datetime
#Task 4: Formatting Dates and Times
# [ ] Write a program that displays the time: (17:39:10) as:
t1 = datetime.time(17,39,10)
# 1) 05:39:10 PM
f1 = t1.strftime("%I:%M:%S %p")
# 2) 17:39:10
f2 = t1.strftime("%H:%M:%S")
print(f1)
print(f2)


# [ ] Write a program that displays the date: (October 23rd 2018) as:
d1 = datetime.date(2018,10,23)

# 1) Oct 23, 2018
f1 = d1.strftime("%b %d, %Y")

# 2) 10/23/18
f2 = d1.strftime("%m/%d/%y")

# 3) 23/October/2018
f3 = d1.strftime("%d/%B/%Y")

# 4) Tuesday October 23
f4 = d1.strftime("%A %B %d")

print(f1)
print(f2)
print(f3)
print(f4)


