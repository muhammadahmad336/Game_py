import random
computer_pick=0
user_pick=0
comp_won=0
user_won=0
opt =["rock","paper","scissors"]
while True:
    user_choice = input("Enter a choice (rock, paper, scissors): or q to quit the game ").lower()
    if user_choice == "q":
        break
    if user_choice not in opt:
        print("Invalid choice. Please choose rock, paper or scissors")
        continue
    random_choise = random.randrange(0,2)
    computer_pick = opt[random_choise]
    print(f"\nComputer chose {computer_pick}")
    if user_choice == "rock" and computer_pick =="scissors":
        print("you won! ")
        user_won +=1
    elif user_choice == "paper" and computer_pick == "rock":
        print("you won! ")
        user_won +=1
    elif user_choice == "scissors" and computer_pick == "paper":
        print("you won! ")
        user_won +=1
    else:
        print("computer won! ")
        comp_won +=1
    print("you won",user_won,"times")
    print("computer won",comp_won,"times")
   