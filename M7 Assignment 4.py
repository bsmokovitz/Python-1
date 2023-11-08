#[1] Write the code to use len() to find the midpoint of randomTIp. Print the halves on separate lines. 

randomTip = "wear a hat when it rains"
midpoint = len(randomTip) // 2
print(randomTip[:midpoint])
print(randomTip[midpoint:])

#[a]Write the code to find the number of “e” and “a” in randomTip.  Print which letter is most frequent. 
print(randomTip.count("e"))
print(randomTip.count("a"))
if randomTip.count("e") > randomTip.count("a"):
    print("e is most frequent")
else:
    print("a is most frequent")


#[2] Write the code to print longWord from the location of the 1st and 2nd “t”. 

longWord = "juxtaposition"

#Hint:  use .find().
print(longWord[longWord.find("t"):longWord.rfind("t")+1])


#[3]Write the code to print each word in a quote.Slice each word out 

quote = "they stumble who run fast"
slice1 = int(quote.find(" ")) 
print(quote[:slice1])
slice2 = int(quote.find(" ", slice1 + 1, len(quote))) 
print(quote[slice1 + 1:slice2])
slice3 = int(quote.find(" ", slice2 + 1, len(quote))) 
print(quote[slice2 + 1:slice3])
slice4 = int(quote.find(" ", slice3 + 1, len(quote))) 
print(quote[slice3 + 1:slice4])
slice5 = int(quote.find(" ", slice4 + 1, len(quote))) 
print(quote[slice4 + 1:])


#[4] Write the program that counts the number of spaces of the phrase
#[4a] Write the program that counts the number of  “a”s in the phrase
#[4b] Write a program that finds the first space and then slices/prints the rest of the phrase.

quote = "they stumble who run fast"

print(quote.count(" "))
print(quote.count("a"))
print(quote[quote.find(" "):])

