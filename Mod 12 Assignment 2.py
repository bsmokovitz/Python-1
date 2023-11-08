#Task 1: Import and Open Local File in Read Mode
city = open("cities.txt", "r")

#Create a external file with the text below:

#Beijing
#Cairo
#London
#Nairobi
#New York City
#Sydney
#Tokyo
 
# Read and print all information into console using read function 
print(city.read())
city.close()


#Task 2: Digits of Pi
#Create an external file with pi below
#Copy and paste the following list of numbers into your external text file:
#pi.txt

#3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273

#read in the number and then round to 2 decimal places.
pi = open("pi.txt", "r")
pi_file = pi.read(7)
pi_file = float(pi_file)
pi_file = round(pi_file, 2)
print(pi_file)
pi.close()



#Task 3: Read to a List
#Read in the cities from before
#using readline() add the cities to a list.
#run a loop that only prints cities that start with a “N”
cities = open("cities.txt", "r")
city_list = []
for city in cities:
    city_list.append(city)
    if city.startswith("N"):
        print(city)
cities.close()

#Task 4: Write a new file	
#create an external file that has your name, age, and grade.

#Task 5: Append to a file	
#Append 3 more cities to the cities file
city = open("cities.txt", "a")
city.write("Paris")
city.write("Rome")
city.write("Dubai")
city.close()

#Submit when complete
