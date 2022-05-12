import random

Run = True
cardNumList = []
userCredit = 0
while True:
    inp = input("Do you wanna play again ? y/n")
    if(inp == "y"):
        level = int(input("Select a difficulty level between 1 and 10: "))
        cardNumList = [False for i in range(level)]
        while True:
            selectedCard = int(input(f"Select a card number between 0 and {level}: "))
            correctCard = random.randint(0,level)
            if correctCard == selectedCard:
                print(f"Congratulations! -> corret answer was {correctCard} !")
                userCredit += level
                print(f"your total credit is -> {userCredit}")
            else:
                print(f"Noo :[ , you lost! -> corret answer was {correctCard} !")
                userCredit = 0
                break
    else:
        print("---GAME OVER---")
        print(f"You have collected {userCredit} credits total")
        break



    
