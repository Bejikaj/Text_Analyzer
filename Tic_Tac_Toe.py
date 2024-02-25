"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Benáček
email: jan.benaczek@seznam.cz
discord: Bejikaj#2628
"""
print ("""
Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
The game fields are numbered:
       
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
             
Let's start the game
----------------------------------------""")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_player = " X "
winner = None
game_is_running = True

def print_board(board):
    print("+---+---+---+")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("+---+---+---+")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("+---+---+---+")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("+---+---+---+")

def player_input(board):      

    while True:

        try:
            inp = int(input(f"Player{current_player}| Please enter your move number: "))  
        except ValueError:
            print("You have not put numerical value! Please put the value from 1 to 9")
            inp = int(input(f"Player{current_player}| Please enter your move number: "))  
    
        if inp >= 1 and inp <= 9 and board[inp-1] == " ":
            board[inp-1] = current_player
            break
        elif inp < 1 or inp > 9:
            print("You choose different number than from the range 1 - 9! Please choose number from 1 to 9")
        elif board[inp-1] != " ":
            print("The position is already occupied, please pick different position!")
        
def check_horizontal(board):
    global winner
    if board[0] == board [1] == board[2] and board [0] != " ":
        winner = board[0]
        return True
    if board[3] == board [4] == board[5] and board [3] != " ":
        winner = board[3]
        return True
    if board[6] == board [7] == board[8] and board [6] != " ":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board [3] == board[6] and board [0] != " ":
        winner = board[0]
        return True
    if board[1] == board [4] == board[7] and board [1] != " ":
        winner = board[1]
        return True
    if board[2] == board [5] == board[8] and board [2] != " ":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board [4] == board[8] and board [0] != " ":
        winner = board[0]
        return True
    if board[2] == board [4] == board[6] and board [2] != " ":
        winner = board[2]
        return True

def check_tie(board):
    global game_is_running
    if " " not in board:
        print_board(board)
        print("It is a tie!")
        game_is_running = False

def check_win():
    global game_is_running
    if check_horizontal(board) or check_row(board) or check_diagonal(board):
        print_board(board)
        print(f"Congratulations, the player{winner}WON!")
        game_is_running = False

def switch_player():
    global current_player
    if current_player == " X ":
        current_player = " O "
    else:
        current_player = " X "

while game_is_running == True:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
