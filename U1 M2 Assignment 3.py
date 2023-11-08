# [ ] fix the sequence of the code to remove the NameError(order problem)


def hat_available(color):
   hat_colors = 'black, red, blue, green, white, grey, brown, pink'
   return(color.lower() in hat_colors)

have_hat = hat_available('green') 
print('hat available is', have_hat)


# create a simple function called bird_available this function should have user input
# print if the bird exist in the menu below using an “in” statement
# call bird_available when complete


def bird_available():
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    bird = input("enter bird type: ")
    bird_exist = bird in bird_types
    print(bird_exist)
 
bird_available()



#Fix the error below

def how_many():
   requested = input("enter how many you want: ")
   return requested


number_needed = how_many()
print(number_needed, "will be ordered")

