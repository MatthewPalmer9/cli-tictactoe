# INITIALIZE GAME BOARD #
board_values = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]

current_player = ''
player1 = ''
player2 = ''
winner = ''

# GAME STARTER
def game_start():
    print('\n')
    print("Welcome to TicTacToe!")
    board_display()
    choose_xo()

# GAME BOARD
def board_display():
    print('\n')
    print(f"{board_values[0]} | {board_values[1]} | {board_values[2]}")
    print("---------")
    print(f"{board_values[3]} | {board_values[4]} | {board_values[5]}")
    print("---------")
    print(f"{board_values[6]} | {board_values[7]} | {board_values[8]}")

# PLAYER CHOOSE X OR O
def choose_xo():
    global player1
    global player2
    global current_player
    acceptable_choices = ['X', 'O']
    choice = 'INVALID'

    while choice not in acceptable_choices:
        choice = input("Player 1 -- Would you like to be X or O? : ").upper()

        if choice not in acceptable_choices:
            print("Sorry, not a valid choice! Try again.")

    player1 = choice 
    acceptable_choices.remove(choice)
    player2 = acceptable_choices[0]

    print(f"Player 1, you are {player1}.")
    print(f"Player 2, you are {player2}.")
    print('\n')
    print("Player 1 goes first...")
    print('\n')

    if player1 == 'X':
        current_player = player1
    else:
        current_player = player2
    
    board_display()




def start_game():
    game_start()

start_game()