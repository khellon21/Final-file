# Define constants for the three choices in the game
print('1 for Rock')
print('2 for Paper')
print('3 for Scissors')
# Import the random module for generating random numbers
import random

ROCK = 1
PAPER = 2
SCISSORS = 3
# Function to get the user's choice
def get_user_choice():
    choice = 0
    while choice not in [ROCK, PAPER, SCISSORS]:
        try:
            choice = int(input("Enter your choice ): "))
            if choice not in [ROCK, PAPER, SCISSORS]:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
    return choice
# Function to get the computer's choice
def get_computer_choice():
    # Return a random number between 1 and 3 (inclusive)
    return random.randint(1,3)
# Function to determine the winner of the game
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == ROCK and computer_choice == SCISSORS) or \
         (user_choice == SCISSORS and computer_choice == PAPER) or \
         (user_choice == PAPER and computer_choice == ROCK):
        return "You win!"
    else:
        return "Computer wins!"
# Main function to run the game
def main():
    continue_game = 'y'
    while continue_game.lower() == 'y':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer chose", computer_choice)
        print(get_winner(user_choice, computer_choice))
        
        continue_game = ''
        while continue_game.lower() not in ['y', 'n']:
            continue_game = input("Do you want to continue? (Y for Yes, N for No): ")
        
    if continue_game.lower() == 'n':
        print("Thank you for playing Rock, Paper, Scissors!")
# Run the main function when the script is executed
if __name__ == "__main__":
    main()
