import random, os,time


def clear():
    os.system('cls')


baseValue = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
             10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
caseValue = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
             10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
holdCase = 0
holdvalue = 0

print("Welcome to Deal or No Deal!")
while True:
    play = input("To play enter start, to quit enter quit\n ")
    if (play != "quit"):
        if (play == "start"):
            clear()
            random.shuffle(caseValue)
            print("Please choose a case...")

            print(cases)
            print(baseValue)




            holdCase = int(input("Enter a number between 1 and 26\n "))


            cases.remove(holdCase)
            holdvalue = caseValue[holdCase - 1]
            caseValue.remove(holdvalue)

            print("You chose case " + str(holdCase))
                
            x = 0
            while x < 6:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[case]))
            
                        cases.remove(case)
                        remove = caseValue[case]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[case])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 5:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[case]))
            
                        cases.remove(case)
                        remove = caseValue[case]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[case])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 4:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[0]))
            
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 3:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[0]))
            
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 2:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[0]))
            
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 1:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)
                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[0]))
            
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 1:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[0]))
            
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 1:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1

                        print("Case " + str(case) + " has $" + str(caseValue[0]))
            
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
            
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")


            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))

            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()

            x = 0
            while x < 1:
                time.sleep(1)
                clear()
                print(cases)
                print(baseValue)

                case = int(input("Enter a number between 1 and 26\n "))
                if (case > 0 and case < 27):
                    if (case in cases):
                        x = x + 1
                        print("Case " + str(case) + " has $" + str(caseValue[0]))
                        cases.remove(case)
                        remove = caseValue[0]
                        baseValue.remove(remove)
                        caseValue.remove(caseValue[0])
                    else:
                        print("Not a valid case")
                else:
                    print("Please enter a valid number")
            deal = 0
            for i in range(len(caseValue)):
                deal += caseValue[i]
                deal = deal / len(caseValue)

            print("The bank offers you $" + str(deal))
    
            takeDeal = input("Do you want to take the deal? Enter yes or no\n ")
            if (takeDeal == "yes"):
                print("You took the deal!")
                clear()
                break
            else:
                print("You did not take the deal")
                time.sleep(1)
                clear()
                switch = input("Do you want to switch cases? Enter yes or no\n")
                if (switch == "yes"):
                    print("You switched cases")
                    print("Case " + str(case) + " has $" + str(caseValue))
                else:
                    print("You did not switch cases")
                    clear()
                    print("Case " + str(holdCase) + " has $" + str(holdvalue))
                    print("Thanks for playing!")
                    break
        else:
            print("Please enter a valid command")
    else:
        clear()
        print("Thanks for playing!")
        break
