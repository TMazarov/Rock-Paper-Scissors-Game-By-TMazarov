from random import randint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_wins = 0
computer_wins = 0
draws = 0

print(f"Welcome to Rock-Paper-Scissor Game!\n"
      f"Please choose one of the following options:\n"
      f"--------------------\n"
      f"[R] for Rock,\n"
      f"[P] for Paper,\n"
      f"[S] for Scissor\n"
      f"[E] If You would like to Exit and print the result!\n"
      f"--------------------")

while True:
    choice = input("Choice: ")
    player_choice = choice.upper()

    if player_choice == "R":
        player_choice = rock
    elif player_choice == "P":
        player_choice = paper
    elif player_choice == "S":
        player_choice = scissors
    elif player_choice == "E":
        print(f"--------------------\n"
              f"Thank you for playing Rock-Paper_Scissor! Your result is below!\n"
              f"--------------------\n"
              f"Player Wins: {player_wins}\n"
              f"Computer Wins: {computer_wins}\n"
              f"Draws: {draws}\n" "--------------------")
        break
    else:
        raise SystemExit("Invalid Input! Please Try Again!")

    computer_choice = randint(1, 3)

    if computer_choice == 1:
        computer_choice = rock
    elif computer_choice == 2:
        computer_choice = paper
    elif computer_choice == 3:
        computer_choice = scissors

    if (player_choice == rock and computer_choice == scissors) or \
            (player_choice == paper and computer_choice == rock) or \
            (player_choice == scissors and computer_choice == paper):
        print("Congratulations! You Win!")
        player_wins += 1
    elif player_choice == computer_choice:
        draws += 1
        print("Draw!")
    else:
        computer_wins += 1
        print("You loose!")
