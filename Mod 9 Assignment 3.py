#Task 1 Combine Lists
# [ ] extend the list commonBirds with list birdsSeen which you must create

commonBirds = ["chicken", "blue jay", "crow", "pigeon"]
birdsSeen = ["hawk", "eagle", "owl",]
commonBirds.extend(birdsSeen)
print(commonBirds)

#Create 2 lists zeroNine and tenOneHundred that contain 1-9, and 10 - 100 by 10's.
zeroNine = [1,2,3,4,5,6,7,8,9]
tenOneHundred = [10,20,30,40,50,60,70,80,90,100]

# [ ] use list addition to concatenate(add) the lists into  a list called allNum and print
allNum = zeroNine + tenOneHundred
print(allNum)


#Task 2 .reverse()
# [ ] create and  print a list of multiples of 5 from 5 to 100(for x in range(5,101,5))
multiples = []
for x in range(5,101,5):
    multiples.append(x)
print(multiples)
# { ] reverse the list and print
multiples.reverse()
print(multiples)

# [ ] Create two lists: fours & moreFours containing multiples of four from 4 to 44
fours = []
moreFours = []
for x in range(4,45,4):
    fours.append(x)
    moreFours.append(x)
print(fours)
print(moreFours)

# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
combineFours = moreFours + fours
combineFours.reverse()
print(combineFours)


#Task 3 .sort() &sorted
 
#[ ] print cites from visitedCities list in alphbetical order using .sort()

visitedCities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
visitedCities.sort()
print(visitedCities)

# [ ] make a sorted copy (sortedCities) of visitedCities list
sortedCities = sorted(visitedCities)

# [ ] remove any city names 5 characters or less from sortedCities
for city in sortedCities:
    if len(city) <= 5:
        sortedCities.remove(city)
print(sortedCities)

# [ ] print visitied cites and sorted cities

visitedCities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
print(visitedCities)
print(sortedCities)
