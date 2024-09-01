import random

exit = False
user_point = 0
computer_point = 0

while exit == False:
    options = ["rock","paper","scissors"]
    print()
    user_input = input("Input rock, paper, scissors or exit: ")
    computer_choice = random.choice(options)
    
    if user_input == "rock":
        if computer_choice == "rock":
            print("Your choice is rock")
            print("computer's choice is rock")
            print("It's a tie")
        elif computer_choice == "paper":
            print("Your choice is rock")
            print("Computer's choice is paper")
            print("You lose, paper covers rock")
            computer_point += 1
        elif computer_choice == "scissors":
            print("Your choice is rock")
            print("Computer's choice is scissors")
            print("You win, rock smashes scissors")
            user_point += 1
    elif user_input == "paper":
        if computer_choice == "rock":
            print("Your choice is paper")
            print("Computer's choice is rock")
            print("You win, paper covers rock")
            user_point += 1
        elif computer_choice == "paper":
            print("Your choice is paper")
            print("Computer's choice is paper")
            print("It's a tie")
        elif computer_choice == "scissors":
            print("Your choice is paper")
            print("Computer's choice is scissors")
            print("You lose, scissors cuts paper")
            computer_point += 1
    elif user_input == "scissors":
        if computer_choice == "rock":
            print("Your choice is scissors")
            print("Computer's choice is rock")
            print("You lose, rock smashes scissors")
            computer_point += 1
        elif computer_choice == "paper":
            print("Your choice is scissors")
            print("Computer's choice is paper")
            print("You win, scissors cuts paper")
            user_point += 1
        elif computer_choice == "scissors":
            print("Your choice is scissors")
            print("Computer's choice is scissors")
            print("It's a tie")
    elif user_input == "exit":
        print()
        print("game ended")
        exit = True
        print("Your total score is",str(user_point) , " and the computer score is", str(computer_point))
        print("The scores are;")
        print("user                                       computer")
        print(" ",user_point,"                                         ",computer_point)
        if user_point > computer_point:
            print("You won the game")
        elif user_point < computer_point:
            print("You lost the game")
        elif user_point == computer_point:
            print("Nobody won, it's a tie")
    else:
        print("Invalid input, you can only input; 'rock','paper','scissors','exit',")