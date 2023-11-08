#Task 1: Iterate through lists using in
# using a Loop do the following
# [ ] create a list of 4 to 6 strings: birds
# print each bird in the list
# [ ]  create a list of 7 integers: player_points
# [ ] print double the points for each point value
# [ ]combine player_points and birds into 1 list, print list.

birds = ["crow", "robin", "sparrow", "bluejay", "cardinal"]
for bird in birds:
    print(bird)
points = [1, 2, 3, 4, 5, 6, 7]
for point in points:
    print(point * 2)
print(birds + points)

#Task 2 : Sort and Filter
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] Using cities from the example above iterate through the list
# [ ] Print only cities starting with "M"
for city in cities:
    if city.startswith("M"):
        print(city)
        

#Task 3 : Sort and Filter
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] Sort the list above alphabetically, print the list
numbers=[3,2,5,2,5,2,6,7,8,9,2,3,4,5]
# [ ] Sort the list in descending order, print the list 
cities.sort()
print(cities)
numbers.sort()
numbers.reverse()
print(numbers)


#Task 4 (program): Paint Stock
#Create list, paint_colors, with 5+ colors
#Get user input of string:color_request
#Using “in” search through the list and determine if the color is found in the list.

paint_colors = ["red", "orange", "yellow", "green", "blue"]
color_request = input("Enter a color: ")
if color_request in paint_colors:
    print("We have that color")
else:
    print("We do not have that color")
    
