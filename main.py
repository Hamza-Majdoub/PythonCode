from getpass import getpass as input
##getpass is password so cant see
print("==Epic Rock Paper Scissors Game!===")
print("-Made by: Hamza Majdoub-")
print("Select your move (R, P, S): ")
print("*Press enter or return after entry*")
print()
print()

player1move = input("Player 1 Move: ")
print()
print()
player2move = input("Player 2 Move: ")
print()
if player1move == 'R' and player2move == 'S':
  print("Rock Beats Paper Player 1 Wins!")
elif player1move == 'S' and player2move == 'R':
  print("Rock Beats Paper Player 2 Wins!")
elif player1move == 'P' and player2move == 'S':
  print("Scissors beat Paper Player 2 Wins!")
elif player1move == 'S' and player2move == 'P':
  print("Scissors beat Paper Player 1 Wins!")
elif player1move == 'P' and player2move == 'R':
  print("Paper Beats Rock Player 1 Wins!")
elif player1move == 'R' and player2move == 'P':
  print("Paper Beats Rock Player 2 Wins!")
elif player1move == 'R' and player2move == 'R':
  print("DRAW!")
elif player1move == 'P' and player2move == 'P':
  print("DRAW!")
elif player1move == 'S' and player2move == 'S':
  print("DRAW!")
else:
  print("Try Again.")