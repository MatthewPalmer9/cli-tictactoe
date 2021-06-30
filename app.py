board = [
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
    placement_handler(current_player, make_choice())

# GAME BOARD
def board_display():
    print('\n')
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('---------')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('---------')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print('\n')

# PLAYER CHOOSE X or O
def choose_xo():
    global player1
    global player2
    global current_player
    acceptable_choices = ['X', 'O']
    choice = 'INVALID'

    while choice not in acceptable_choices:
        choice = input("Player 1, do you want to be X or O? (X/O) : ").upper()

        if choice not in acceptable_choices:
            print("Sorry, that is and invalid choice!")
        
    player1 = choice
    acceptable_choices.remove(choice)
    player2 = acceptable_choices[0]

    print(f"Player 1, you are {player1}!")
    print(f"Player 2, you are {player2}!")
    print('\n')
    print("Please remember, X goes first! :)")
    print('\n')

    if player1 == 'X':
        current_player = player1
    else:
        current_player = player2

    board_display()


# CHOICE MAKER
def make_choice():
    choice = 'WRONG'
    acceptable_range = range(1,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input(f"Player {current_player}, Please choose a number (1-9) : ")

        # DIGIT CHECK
        if choice.isdigit() == False or choice == '':
            print("Sorry, that is not a digit!")
            make_choice()

        # RANGE CHECK
        if choice.isdigit():
            if int(choice) in acceptable_range :
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False
        
        # POSITION CHECK
        if board[int(choice)-1] != ' ':
            print("Sorry, that spot is already filled! Please choose another.")
            return make_choice()
        
    return int(choice)

# WINNER CHECK
def winner_check():
    global winner

    # PLAYER 1 WINNER CHECK
    if board[0] == player1 and board [1] == player1 and board[2] == player1:
        winner = player1
    elif board[3] == player1 and board [4] == player1 and board[5] == player1:
        winner = player1
    elif board[6] == player1 and board [7] == player1 and board[8] == player1:
        winner = player1
    elif board[0] == player1 and board [4] == player1 and board[8] == player1:
        winner = player1
    elif board[6] == player1 and board [4] == player1 and board[2] == player1:
        winner = player1
    elif board[0] == player1 and board [3] == player1 and board[6] == player1:
        winner = player1
    elif board[1] == player1 and board [4] == player1 and board[7] == player1:
        winner = player1
    elif board[2] == player1 and board [5] == player1 and board[8] == player1:
        winner = player1

    if board[0] == player2 and board [1] == player2 and board[2] == player2:
        winner = player2
    elif board[3] == player2 and board [4] == player2 and board[5] == player2:
        winner = player2
    elif board[6] == player2 and board [7] == player2 and board[8] == player2:
        winner = player2
    elif board[0] == player2 and board [4] == player2 and board[8] == player2:
        winner = player2
    elif board[6] == player2 and board [4] == player2 and board[2] == player2:
        winner = player2
    elif board[0] == player2 and board [3] == player2 and board[6] == player2:
        winner = player2
    elif board[1] == player2 and board [4] == player2 and board[7] == player2:
        winner = player2
    elif board[2] == player2 and board [5] == player2 and board[8] == player2:
        winner = player2
    
    return winner

def placement_handler(player, choice):
    global current_player
    board[choice-1] = player

    board_display()
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    
    winner = winner_check()
    if winner == 'X' or winner == 'O':
        print(f"Congratulations, Player {winner}! YOU WIN! Game over.")
        play_again()
    else:
        placement_handler(current_player, make_choice())

def play_again():
    gameon = 'INVALID'
    acceptable_choices = ['Y', 'N']

    while gameon not in acceptable_choices:
        gameon = input("Play again? (Y/N) : ").upper()

    if gameon not in acceptable_choices:
        print("Sorry, invalid response. Please choose Y or N...")

    if gameon == 'Y':
        game_start()
    else:
        print("Goodbye! Thanks for playing!")

game_start()