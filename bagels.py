#Hello thank you for using my program
#This works with Python3
#What does this program do?: This is a deductive logic game
#What is the game rules: The program creates a random 3 digit number try to guess what it is here are some hints!
#Pico: One digit is correct but in the wrong position.
#Fermi: One digit is correct and in the right position.
#Bagels: No digit is correct
#This is project 1 or chapter 1 from "THE BIG BOOK OF SMALL PYHTON PROJECTS"
#Thanks for using!


from random import randint
print("Bagels, a deductive logic game.")
print("By bluedrummer  or https://github.com/bluedrummer")
print()
print("I am thinking of a digit 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say:     That means:")
print("  Pico          One digit is correct but in the wrong position.")
print("  Fermi         One digit is correct and in the right position.")
print("  Bagels        No digit is correct.")
print("I have thought up a number.")
print("You have 10 guesses to get it.")
playing_status = True
while playing_status == True:
    playing_status = True
    number = 0
    while True:
        good_number = False
        number = randint(100, 987)
        number = str(number)
        good_number_count = 0
        for i in range(0, len(number)):
            if number.count(number[i]) == 1:
                good_number_count += 1
            if good_number_count == 3:
                good_number = True
                break
        if good_number == True:
            break

    for i in range(0, 10):
        print(f"Guess #{i + 1}:")
        while True:
            guess_number = input()
            if len(guess_number) == 3:
                break
            if len(guess_number) != 3:
                print("Please retry as number is not 3 digits")
        type_of_guess = ""
        digits_guessed_right=0
        for l in range(0, len(number)):
            for d in range(0, len(number)):
                if guess_number[l] == number[d]:
                    digits_guessed_right += 1
                    if l == d:
                        type_of_guess = type_of_guess + " " + "Fermi"
                        break
                    else:
                        type_of_guess = type_of_guess + " " + "Pico"
                        break

        if digits_guessed_right == 0:
            type_of_guess = "Bagels"
        print(type_of_guess.lstrip())

        if guess_number == number:
            print("You got it!")
            print("Would you like to play again? (yes or no)")
            player_status = input().lower()
            if player_status == "no":
                print("Thanks for playing (bluedrummer at github)")
                playing_status = False
                break
            if player_status == "yes":
                break

        if i == 9 and guess_number != number:
            print("You didint get the number.")
            print(f"The number was {number}")
            print("Would you like to play again? (yes or no)")
            player_status = input().lower()
            if player_status == "no":
                print("Thanks for playing (bluedrummer at github)")
                playing_status = False
                break
            if player_status == "yes":
                break
