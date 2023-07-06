import random

print("Rock Paper Scissors shoot.")

player_1 = input("Player_1, choose either Rock, Paper, or Scissors: ")

while player_1 != "off":
    choices = ['Rock', 'Paper', 'Scissors']
    player_2 = random.choice(choices)

    if player_1 == 'Scissors' and player_2 == 'Paper':
        print("Player_1, you have won this match!")
    elif player_1 == 'Scissors' and player_2 == 'Rock':
        print("Player_2, you have won this match!")
    elif player_1 == 'Paper' and player_2 == 'Scissors':
        print("Player_2, you have won this match!")
    elif player_1 == 'Paper' and player_2 == 'Rock':
        print("Player_1, you have won this match!")
    elif player_1 == 'Rock' and player_2 == 'Paper':
        print("Player_2, you have won this match!")
    elif player_1 == 'Rock' and player_2 == 'Scissors':
        print("Player_1, you have won this match!")
    else:
        print("Tie breaker!")
    
    game = input("Do you want to play another game? (yes/no): ")
    if game == 'yes':
        player_1 = input("Player_1, choose either Rock, Paper, or Scissors: ")
    else:
        break
