# INITIALIZE GAME BOARD #
board_values = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]

def game_board():
    print('\n')
    print(f"{board_values[0]} | {board_values[1]} | {board_values[2]}")
    print("---------")
    print(f"{board_values[3]} | {board_values[4]} | {board_values[5]}")
    print("---------")
    print(f"{board_values[6]} | {board_values[7]} | {board_values[8]}")



def start_game():
    game_board()

start_game()