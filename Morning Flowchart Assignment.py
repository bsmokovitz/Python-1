wakeUp = input("Did you wake up for school today?\n")
if wakeUp.lower() == "yes":
    brushTeeth = input("Did you Brush Your teeth?\n")
    if brushTeeth.lower() == "yes":
        breakfast = input("What did you have for breakfast?\n")
        if breakfast.lower() == "Cereal":
            print("Cereal is Fantastic")
        elif breakfast.lower() == "Pancakes":
            print("Wow, who has time for pancakes in the morning?\n")
        elif breakfast.lower() == "Eggs":
            print("Eggs are good protine ")
        else:
            print("Sounds good ")
    else:
        print("Gross ")
else:
    print("Set an Alarm ")