
player_one = input("player one choose rock, paper, scissor? \n")


#prompt for player one

while player_one != "rock" or "paper" or "scissor":

    if player_one == "rock":
        break
    if player_one == "paper":
        break
    if player_one == "scissor":
        break

    else:
        player_one = input("player one choose rock, paper, scissor? \n")


#prompt for player two
player_two = input(" player two choose rock, paper, scissor? \n")

while player_two != "rock" or "paper" or "scissor" :
    if player_two == "rock":
        break
    if player_two == "paper":
        break
    if player_two == "scissor":
        break

    else:
        player_two = input("player two choose rock, paper, scissor? \n")

if (player_one == "rock" and player_two == "rock"):
    print("Tie")

if (player_one == "rock" and player_two == "paper"):
    print("player two wins")

if (player_one == "rock" and player_two == "scissor"):
    print("player one wins")

if (player_one == "scissor" and player_two == "scissor"):
    print("tie")

if (player_one == "scissor" and player_two == "paper"):
    print("player one wins")

if (player_one == "scissor" and player_two == "rock"):
    print("player two wins")

if (player_one == "paper" and player_two == "paper"):
    print("tie")

if (player_one == "paper" and player_two == "scissor"):
    print("player two wins")

if (player_one == "paper" and player_two == "rock"):
    print("player two wins")