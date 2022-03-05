#By bluedrummer at github or https://github.com/bluedrummer
#This works with python3
#What does this program do? This Japenese game call Cho-Han: two dice are rolled
#and the player must guess if the total of the two dice are even or odd number (a dice has only 6 number!).
#This is a project from chatper 10 or project 10 of Big Book Of Small Python Projects
#Enjoy!

print('''By bluedrummer at github or https://github.com/bluedrummer
This works with python3
What does this program do?
This is a Japenese game called Cho-Han. Two dice are rolled
and the player must guess if the total of the two dice are an even or odd number.
This is a project from chatper 10 or project 10 of Big Book Of Small Python Projects
Enjoy!''')

import sys, random

purse = 5000

while True:
    print(f"You have {purse} mon. How much do you bet? (Or QUIT)")
    while True:
        pot = input()
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number")
        elif int(pot) > purse:
            print("You dont have enough money to make that bet. :(")
        else:
            pot = int(pot)
            break

    dice1 = random.randint(0, 6)
    dice2 = random.randint(0, 6)

    print("The dealer swirls the cup and you hear the the dice rattle.")
    print("The dealer slams the cup on the floor")
    print("He asks whats your bet?")
    print()
    print("     CHO (even) or  HAN (odd)?")

    while True:
        bet = input().upper()
        if bet != "CHO" and bet != "HAN":
            print("Please enter either CHO or HAN." )
            continue
        else:
            break

    print("The dealer lifts the cup to reveal")
    print(f"{dice1} - {dice2}")

    rollIsEven = (dice1 + dice2) % 2 == 0

    if rollIsEven:
        correctBet = "CHO"
    else:
        correctBet = "HAN"

    playerWon = bet = correctBet

    if playerWon:
        print(f"You Won! You Take {pot} mon.")
        purse = purse + pot
        print(f"The house collects a {pot // 10} mon fee.")
        purse = purse - (pot // 10)
    else:
        purse = purse - pot
        print("You lost!")

    if purse == 0:
        print("You have run out of money!")
        print("Thanks for playing!")
        sys.exit()
