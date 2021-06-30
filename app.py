import speech_recognition

# INITIALIZE GAME BOARD #
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
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

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

# CHOICE LISTENER
def choice_listener():
    acceptable_answers = [
        'play top left',
        'play top middle',
        'play top right',
        'play middle left',
        'play middle',
        'play middle right',
        'play bottom left',
        'play bottom middle',
        'play botom right'
    ]
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
            print("Please choose your position (ex. 'play middle', 'play top left', 'play middle right', 'play bottom middle'): ")
            audio = recognizer.listen(source)
            choice = recognizer.recognize_google(audio)
            print(f"You said: {choice}")

            if choice in acceptable_answers:
                return acceptable_answers.index(choice)
            else:
                print("Sorry, invalid choice. Try again!")
                choice_listener()

# CHOICE MAKER
def make_choice():
    choice = 'WRONG'
    acceptable_range = range(0,8)

    while choice.isdigit() == False or choice not in acceptable_range:
        choice_listener()


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
        print(f"Congratulations, player {winner}! YOU WON! Game over.")
    else:
        placement_handler(current_player, make_choice())



def start_game():
    game_start()

start_game()