from random import randint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

print(f"Welcome to Rock-Paper-Scissor Game!\n"
      f"Please choose one of the following options:\n"
      f"--------------------\n"
      f"[R] for Rock,\n"
      f"[P] for Paper,\n"
      f"[S] for Scissors\n"
      f"--------------------")
player_choice = input("Choice: ")

if player_choice == "R":
    player_choice = rock
elif player_choice == "P":
    player_choice = paper
elif player_choice == "S":
    player_choice = scissors
else:
    raise SystemExit("Invalid Input! Please Try Again!")

computer_choice = randint(1, 3)

if computer_choice == 1:
    computer_choice = rock
elif computer_choice == 2:
    computer_choice = paper
elif computer_choice == 3:
    computer_choice = scissors

if (player_choice == rock and computer_choice == scissors) or (player_choice == paper and computer_choice == rock) or (player_choice == scissors and computer_choice == paper):
    print("Congratulations! You Win!")
elif player_choice == computer_choice:
    print("Draw!")
else:
    print("You loose!")
