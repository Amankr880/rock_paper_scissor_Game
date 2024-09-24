import random


while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    userChoice = int(input("Enter your choice: "))

    while userChoice > 3 or userChoice < 1:
        userChoice = int(input('Enter a valid choice please : '))

    if userChoice == 1:
        choice_name = 'Rock'
    elif userChoice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    compChoice = random.randint(1, 3)

    if compChoice == 1:
        compChoice_Name = 'Rock'
    elif compChoice == 2:
        compChoice_Name = 'Paper'
    else:
        compChoice_Name = 'Scissors'

    print("Computer choice is:", compChoice_Name)

    if userChoice == compChoice:
        result = "DRAW"
    elif (userChoice == 1 and compChoice == 2) or (compChoice == 1 and userChoice == 2):
        result = 'Paper'
    elif (userChoice == 1 and compChoice == 3) or (compChoice == 1 and userChoice == 3):
        result = 'Rock'
    elif (userChoice == 2 and compChoice == 3) or (compChoice == 2 and userChoice == 3):
        result = 'Scissors'

    # Print the result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")
