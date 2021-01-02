import os, random
import copy
import string
# import keyboard

ascii_title = """
   ___       _   _   _           _     _           
  / __\ __ _| |_| |_| | ___  ___| |__ (_)_ __  ___ 
 /__\/// _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
/ \/  \ (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
\_____/\__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                        |_|"""

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_title():
    print(ascii_title)

def display_player_one():
    print("Player 1:")

def display_player_two():
    print("Player 2:")

def display_player_computer():
    print("Computer:")

def main_menu():
    clear_console()
    display_title()
    print("Welcome to Battleships!")
    print("Game modes:")
    print("1. Single player")
    print("2. Multiplayer")
    print()
    game_mode = ask_for_a_game_mode(force_valid_input = True)
    print()
    clear_console()
    display_title()
    board_size = ask_for_a_board_size(force_valid_input = True)
    length = changing_board_size_to_length(board_size)
    width = changing_board_size_to_width(board_size)
    if game_mode == 1:
        player_vs_computer_placement_phase(length, width)
    if game_mode == 2:
        player_vs_player_placement_phase(length, width)

# def init_board(length, width):
#     board = []
#     for board_counter in range(0, width):
#         board.insert(board_counter, length * "0")
#     return board

def init_board(length, width):
    board = []
    # new_board = []
    # for new_board_counter in range(0, width):
    #     new_board.insert(new_board_counter, "0")
    for board_counter in range(0, width):
        board.insert(board_counter, ["0"] * length)
    return board

def decorator(board):
    total_length = (((len(board) - 1) * 3) + 1)
    total_length_for_ten = (((len(board) - 1) * 3) + 3)
    if len(board) < 10:
        print(end = "    ")
        for counter in range(0, total_length):
            print("-", end = "")
    else:
        print(end = "   ")
        for counter in range(0, total_length_for_ten):
            print("-", end = "")
    print()

def print_number_coordinates(board):
    ascii_number = 49 #cyfra oznaczająca cyfrę "1" w ASCII
    print(end = "    ")
    for counter in range(0, len(board)):
        if ascii_number in range(49, 58):
            if counter < (len(board) - 1):
                char_number = chr(ascii_number)
                print(char_number, end = "  ")
                ascii_number += 1
            else:
                char_number = chr(ascii_number)
                print(char_number)
                ascii_number += 1
        else:
            print("10")

def is_number_board_size(user_input):
    if user_input == "quit":
        exit()
    if user_input.isnumeric():
        if 5 <= int(user_input) <= 10:
            return int(user_input)
        else:
            print("Invalid input! (must be between 5-10)")
    else:
        print("This is not a number!")
        return None

def ask_for_a_board_size(force_valid_input):
    while True:
        user_input = input('Please provide a board size that You want to play with (5-10): ')
        user_value = is_number_board_size(user_input)
        if isinstance(user_value, int):
            return user_value
        if force_valid_input == False:
            return None

def is_number_game_mode(user_input):
    if user_input == "quit":
        exit()
    if user_input.isnumeric():
        if 1 <= int(user_input) <= 2:
            return int(user_input)
        else:
            print("Wrong input! Think again and choose wisely!")
    else:
        print("Wrong input! Think again and choose wisely!")
        return None

def ask_for_a_game_mode(force_valid_input):
    while True:
        user_input = input('Please provide a game mode (1/2): ')
        user_value = is_number_game_mode(user_input)
        if isinstance(user_value, int):
            return user_value
        if force_valid_input == False:
            return None

def print_alphabet_coordinates(board):
    ascii_letter = 65 #cyfra oznaczająca literę "A" w ASCII
    place_holder = 0
    for alphabet_counter in range(0, len(board[0])):
        char_alpha = chr(ascii_letter)
        print(char_alpha + " |", end = " ")
        ascii_letter += 1
        for board_counter in range(0, len(board[0])):
            if board_counter != (len(board[0]) - 1):
                print(board[place_holder][board_counter], end = "  ")
            else:
                print(board[place_holder][board_counter], end = " |")
                print()
        place_holder += 1

def print_board(board):
    print_number_coordinates(board)
    decorator(board)
    print_alphabet_coordinates(board)
    decorator(board)

def player_vs_player_placement_phase(length, width):
    player_one_board = init_board(length, width)
    total_number_of_ships = 10
    actual_number_of_ships = 0
    # player_two_board = init_board(length, width)
    while actual_number_of_ships < 10:
        clear_console()
        display_title()
        print("Placement phase")
        print()
        display_player_one()
        print()
        print_board(player_one_board)
        print()
        player_one_board = place_ship(player_one_board, 1)
        # number_of_ships += 1

def player_vs_computer_placement_phase(length, width):
    player_one_board = init_board(length, width)
    computer_board = init_board(length, width)
    clear_console()
    display_title()
    display_player_one()
    print()
    print_board(player_one_board)
    print()
    display_player_computer()
    print()
    print_board(computer_board)

def changing_board_size_to_length(board_size):
    if board_size == 5:
        length = 5
        return length
    if board_size == 6:
        length = 6
        return length
    if board_size == 7:
        length = 7
        return length
    if board_size == 8:
        length = 8
        return length
    if board_size == 9:
        length = 9
        return length
    if board_size == 10:
        length = 10
        return length

def changing_board_size_to_width(board_size):
    if board_size == 5:
        width = 5
        return width
    if board_size == 6:
        width = 6
        return width
    if board_size == 7:
        width = 7
        return width
    if board_size == 8:
        width = 8
        return width
    if board_size == 9:
        width = 9
        return width
    if board_size == 10:
        width = 10
        return width

def play_again():
    print()
    user_input = input("Want to play again? (Y/N): ")
    if user_input == "Y" or user_input == "y":
        play()
    if user_input == "N" or user_input == "n":
        exit()
    if user_input != "Y" or "N" or "y" or "n":
        play_again()

def mark(board, row, col, symbol):
    ''' Marks element in board with a symbol '''
    ''' 0 - undiscovered, M - missed, H - hit, S - sunk '''

    board[row][col] = symbol

    return board

def get_move(board):

    #determining board rows and cols
    num_rows = len(board)
    num_cols = len(board[0])

    #assigning letters to available rows
    letters = string.ascii_uppercase[:num_rows]

    while True:
        move = input("Please, pick a move eg. A2, or type 'quit' to exit: ")

        if move.lower() == 'quit':
            exit()

        if len(move) != 2:
            print('Invalid move. Please try again.')
            continue

        if move[0].upper() not in letters and move[1] not in range(num_cols-1):
            print('Your move is outside the board. Please try again.')
            continue
        else:
            row = letters.index(move[0].upper()) #checks position of an uppercased letter in letters list
            col = int(move[1]) - 1
        if not '0' in board[row][col]:
            print('This place is already taken. Please try again.')
            continue
        else:
            break

    return row, col

# def show_waiting_screen():
#     clear_console()
#     print("\n\n\n ========= Next player's placement phase ==========\n\n\n")
#     keyboard.read_key()
#     clear_console()

def place_ship(board, ship_length):
    ''' Places ship of defined length on board by user input. '''
    ''' TO DO: don't let place ship next to each other '''


    print(f'You are now placing a ship {ship_length} places long.')
    if ship_length > 1:
        direction = ''
        while direction not in ['h', 'v']:
            direction = input("Please specify direction of the ship. It could be horizontal 'h' or vertical 'v': ")
    
    print("Please pick ship's starting point.")
    row, col = get_move(board)

    board_copy = copy.deepcopy(board)

    if ship_length > 1:
        try:
            for ship_element in range(ship_length):
                if direction == 'h':
                    mark(board_copy, row, col + ship_element, 'x')
                else:
                    mark(board_copy, row + ship_element, col, 'x')

        except IndexError:
            print('Your ship exceeds the sea! Try again.')
            place_ship(board, ship_length)
        
        else:
            board = board_copy
    
    else:
        mark(board_copy, row, col, 'x')
        board = board_copy

    return board

def play():
    main_menu()
    play_again()

if __name__ == "__main__":
    clear_console()
    play()