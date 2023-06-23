print("Rock Paper Scissors shoo.")

player_1 = input("Player_1 Choose ethier Rock Paper or Scissors:")
player_2 = input("Player_2 Choose ethier Rock Paper or Scissors:")

while player_1 != "off":
    if player_1 == 'Scissors' and player_2 == 'Paper':
        print("Player_1 you have won this match!!!")
    elif player_1 == 'Scissors' and player_2 == 'Rock':
        print("Player_2 you have won this match!!!")
    elif player_1 == 'Paper' and player_2 == 'Scissors':
        print("Player_2 you have won this match!!!")
    elif player_1 == 'Paper' and player_2 == 'Rock':
        print("Player_1 you have won this match!!!")
    elif player_1 == 'Rock' and player_2 == 'Paper':
        print("Player_2 you have won this match!!!")
    elif player_1 == 'Rock' and player_2 == 'Scissors':
        print("Player_1 you have won this match!!!")
    else:
        print("Tie braker")
    
    
    game = input("Want to  play another game:")
    if game == 'yes':
        player_1 = input("Player_1 Choose ethier Rock Paper or Scissors:")
        player_2 = input("Player_2 Choose ethier Rock Paper or Scissors:")
    