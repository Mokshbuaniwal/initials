import random

# Get user input
user = input("Enter Rock, Paper, or Scissors: ")

# user input while if 
while user not in ['rock', 'paper', 'scissors']:
    print("Invalid choice! Try again.")
    user = input("Enter Rock, Paper, or Scissors: ")

# Generate computer choice
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# Show choices
print(f"You chose: {user}")
print(f"Computer chose: {computer_choice}")

if user == computer_choice:
    print("It's a tie!")
elif (user == 'rock' or 'ROCK' and computer_choice == 'scissors') or \
     (user == 'paper' and computer_choice == 'rock') or \
     (user == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")