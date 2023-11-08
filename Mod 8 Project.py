def list_o_matic():
    if input_animal == "":
        animals.pop()
    else:
        if input_animal in animals:
            animals.remove(input_animal)
            return animals.append(input_animal)
        else:
            animals.append(input_animal)

animals = ['cat', 'dog', 'monkey']
while True:
    if len(animals) == 0:
        print("No more animals! GOODBYE!")
        break
    elif len(animals) >= 1:
        input_animal = input('Enter an animal: ')
        if input_animal == "Quit":
            break
        else:
            list_o_matic();
            print(animals)

