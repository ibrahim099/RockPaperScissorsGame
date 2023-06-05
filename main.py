import random
def play_game():
    print("Welcome to Rock Paper Scissors!")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    print("You chose:", player_choice)
    print("The computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock' and computer_choice == 'scissors' or \
         player_choice == 'paper' and computer_choice == 'rock' or \
         player_choice == 'scissors' and computer_choice == 'paper':
         print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

play_game()


