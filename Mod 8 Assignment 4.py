#Task 1
ftBones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
#Print ftBones list
#Delete “cuboid” from ftBones
#Reprint list
print(ftBones)
del ftBones[2]
print(ftBones)


#Task 2
#delete “navicular” from list
#reprint list (before)
#check for deletion of “cuboid” and “navicular”
ftBones.remove("navicular")
print(ftBones)

#Task 3
#pop() and print the first and last items from the ftBones list
ftBones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
#print the remaining list
ftBones.pop()
print(ftBones)


#Task 4
#Remove one “Poodle” from the list: dogs, 
#Print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
dogs.remove("Poodle")
print(dogs)


