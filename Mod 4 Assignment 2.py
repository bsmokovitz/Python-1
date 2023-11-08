#[1] Create a simple function called home().  The function should return your address.  #Make sure your print the function since return doesn’t print
def home():
    return "3710 Colby Chase Drive, Apex NC 27539"
print(home())

#[2] Create a function called day().  The function should have user input inside the function asking “What day is it?”  then the function returns “Have a great”_____(user input).  Call and print the function.
def day():
    day=input("What day is it?")
    return "Have a great " + day.upper()
print(day())

#[3] Finish the function make_doctor() below with full_name argument from user input - then print the return value
def make_doctor(full_name):
    full_name=input("What is your full name?")
    return "Dr. " + full_name.title()
print(make_doctor(""))

# [4] add a 3rd period parameter to make_schedule function below

def make_schedule(period1, period2, period3):
   schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
   return schedule
   
student_schedule = make_schedule("mathematics", "history", "science")
print("SCHEDULE:", student_schedule)

