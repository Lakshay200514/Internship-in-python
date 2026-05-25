import random   
Uchoice=0
Cchoice=0
print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        Uchoice += 1
    else:        
        Cchoice += 1
    if(Uchoice==3):
        print("Congratulations! You won the game!")
        break
    elif(Cchoice==3):
        print("Computer won the game! Better luck next time.")
        break
