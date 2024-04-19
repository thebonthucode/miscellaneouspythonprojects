import random

wins = 0
lose = 0
draws = 0

while True:
    user = input("Welcome. Choose rock(r), paper(p), or scissors(s): ")
    rps = ["r", "p", "s"]
    computer = rps[0] or rps[1] or rps[2]
    print("The computer chose " + str(computer))
    if user == computer:
        print("It's a draw!")
        draws += 1
    elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        print("You won!")
        wins += 1
    else:
        print("You lost!")
        lose += 1

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print("Wins: " + wins + ",Losses: " + lose + ",Draws: " + draws)
        break
