# define constants


PLAYER_1 = "\u274c"
PLAYER_2 = "\u2b55"
EMPTY_CELL = "\u2b1c"
MAX_BOARD_SIZE = 15


# functions
def create_game_board():
    board_size = 0
    while board_size not in range(3, MAX_BOARD_SIZE+1):
        board_size = int(input("Enter board size: "))
        pass
    board = [[EMPTY_CELL for i in range(board_size)]
             for j in range(board_size)]

    return board


def draw_board(board):
    board_string = ""

    # create column titles
    board_string += "\t"
    for i in range(len(board)):  # board width = board height
        board_string += chr(65 + i) + "  "
        pass
    board_string += "\n"

    # add board with row numbers
    for row_index in range(len(board)):  # board width = board height
        # add next row
        board_string += str(row_index + 1) + "\t"
        for cell_index in range(len(board)):
            board_string += board[row_index][cell_index] + " "
            pass
        board_string += "\n"
        pass
    return board_string


def next_move(board, player):
    # Request coordinates move

    while True:

        user_input = input(f"Enter coordinates ({player}) [A:3]: ").upper()

        if len(user_input) != 3:
            print(
                "Must be no more than 3 characters separated by \":\"\n Please try again.")
            continue
        if ord(user_input.split(":")[0]) not in range(65, 65+len(board)):
            print(
                f"The first character must be in the range [ A - {chr(65 + len(game_board) - 1)}].\n Please try again.")
            continue
        if ord(user_input.split(":")[1]) not in range(49, 49+len(board)):
            print(
                f"The second character must be a number from [{1} - {1+len(game_board) - 1}]! \nPlease try again.")
            continue

        row_index = int(user_input[2]) - 1
        cell_index = ord(user_input[0]) - 65

        if board[row_index][cell_index] != EMPTY_CELL:
            print("Invalid input. Please try again.")
            continue

        break

    # Change game board
    game_board[row_index][cell_index] = player
    return


def game_over(board, counter):
    # Check epmty cells
    # if counter >= len(board)**2:
    #     return True

    # Check rows
    for row in game_board:
        if row.count(current_player) == len(row):
            print(f"Player {current_player} wins!")
            return True
        pass

    # Check columns
    for i in range(len(game_board)):
        column = []
        for row in game_board:
            column.append(row[i])
            pass
        if column.count(current_player) == len(column):
            print(f"Player {current_player} wins!")
            return True
        pass

    # Check diagonals
    diagonal_1 = []
    diagonal_2 = []
    for i in range(len(game_board)):
        diagonal_1.append(game_board[i][i])
        diagonal_2.append(game_board[i][len(game_board) - 1 - i])
        pass
    if diagonal_1.count(current_player) == len(diagonal_1):
        print(f"Player {current_player} wins!")
        return True
    if diagonal_2.count(current_player) == len(diagonal_2):
        print(f"Player {current_player} wins!")
        return True
    return False


current_player = PLAYER_1
move_counter = 0
game_board = create_game_board()

while not game_over(game_board, move_counter):

    move_counter += 1

    print(draw_board(game_board))

    next_move(game_board, current_player)

    if game_over(game_board, move_counter):
        break

    # Switch user
    current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

    pass
