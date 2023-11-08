#Task 1: Creating timedelta objects
from datetime import timedelta,date,datetime,time
#[1]Create a ‘timedelta’ object called td that contains: 2 hours, 3 minutes and 1 week
td = timedelta(hours=2, minutes=3, weeks=1)
#Print td
print(td)
#[2]Use a ‘timedelta’ object to find out how many days are left until your upcoming birthday
today = date.today()
birthday = date(today.year, 12, 1)
print(birthday - today)


#Task 2: Performing Date Arithmetic
#Write a program to compute the date 3 weeks before your birthday
today = date.today()
birthday = date(today.year, 12, 1)
print(birthday - timedelta(weeks=3))

#Task 3: Comparing datetime Objects
#Write a program to find out if 4th of July of this year has passed or not
from datetime import date

today = date.today()
july4th = date(today.year, 11, 17)
if july4th < today:
    print("4th of July has passed")
else:
    print("4th of July has not passed")

#Task 4: Creating Useful Applications
# [ ] Complete the following program to find out if you are closer to the current year's June or December solstice
import datetime
# Define today's date
now = datetime.date.today()
 
# Define the December solstice
dec_solstice = datetime.date(now.year, 12, 21)
 
# Define the June solstice
jun_solstice = datetime.date(now.year, 6, 21)
 
# Find out which solstice is closer
if now - jun_solstice < dec_solstice - now:
    print("June solstice is closer")
else:
    print("December solstice is closer")



