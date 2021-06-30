# INITIALIZE GAME BOARD #
board_values = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]

player1 = ''
player2 = ''

def game_board():
    print('\n')
    print(f"{board_values[0]} | {board_values[1]} | {board_values[2]}")
    print("---------")
    print(f"{board_values[3]} | {board_values[4]} | {board_values[5]}")
    print("---------")
    print(f"{board_values[6]} | {board_values[7]} | {board_values[8]}")

def choose_playing_position():
    global player1
    global player2
    answer = input("Player 1 -- Would you like to be X or O? : ").upper()

    while answer not in ['X', 'O']:
        print("Sorry, not a valid choice \n")
        answer = input("Player 1 -- Would you like to be X or O? : ").upper()

    print('\n')
    if answer == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'

    print(f"Player 1, you are {player1}.")
    print(f"Player 2, you are {player2}.")
    print('\n')
    print("Player 1 goes first...")
    game_board()
    print('\n')




def start_game():
    game_board()
    choose_playing_position()

start_game()