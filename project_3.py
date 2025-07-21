import random

# Get user input
user = input("Enter Rock, Paper, or Scissors: ").lower()

# Validate user input
while user not in ['rock', 'paper', 'scissors']:
    print("Invalid choice! Try again.")
    user = input("Enter Rock, Paper, or Scissors: ").lower()

# Generate computer choice
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# Show choices
print(f"\nYou chose: {user}")
print(f"Computer chose: {computer_choice}")

# Determine winner
if user == computer_choice:
    print("It's a tie!")
elif (user == 'rock' and computer_choice == 'scissors') or \
     (user == 'paper' and computer_choice == 'rock') or \
     (user == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
