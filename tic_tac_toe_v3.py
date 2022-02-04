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
    board = [[EMPTY_CELL for i in range(board_size)] for j in range(board_size)]
    return board

def draw_board(board):
    board_string = ""
    """
        A B C D E \n
    1   . . . . . \n
    2   . x . . . \n
    3   . . . o . \n
    4   . x . . . \n
    5   . . . . . \n
    """
    # create column titles
    board_string += "\t"
    for i in range(len(board)): # board width = board height 
        board_string += chr(65 + i) + "  "
        pass
    board_string += "\n"
    
    # add board with row numbers
    for row_index in range(len(board)): # board width = board height 
        # add next row
        board_string += str(row_index + 1) + "\t"
        for cell_index in range (len(board)):
            board_string += board[row_index][cell_index] +  " "
            pass         
        board_string += "\n"
        pass
    return board_string

def do_next_move(board, player): # 2 formal parameters
    # Request move coordinates
    
    while True:        
        user_input = input (F"Enter your move ({player}): [A:3]").upper()  # "d:3"
        # check: split(":")[0] - letter, split(":")[1] - number
        # if not user_input.split(":")[0].isalpha() : continue 
        # if not user_input.split(":")[1].isnumeric(): continue
        if len(user_input) != 3:
            print ("Input length incorrect")
            continue
        if ord(user_input.split(":")[0]) not in range(65, 65 + len(board)): continue
        if ord(user_input.split(":")[1]) not in range(49, 49 + len(board)): continue
        row_index = int(user_input[2]) - 1
        col_index = ord(user_input.split(":")[0]) - 65
        if board[row_index][col_index] != EMPTY_CELL:  continue
        break
    
    # Change game board
    game_board[row_index][col_index] = player 
    
    pass

def game_over(board, counter): # yes? no?
    
    # check empty cells -> return True
    if counter >= len(board) * len(board): return True
    
    # check rows
    # for .......:
    player1_won = len(board) * PLAYER_1 # type - string, xxxx
    player2_won = len(board) * PLAYER_2
    for row in range(len(board)): # Start loop - rows
        """
        xxxx
        0000
        """
        row_to_check = ""
        for cell in range(len(board[row])): # start next row loop (cells)
            row_to_check += board[row][cell]       
            pass        
        if row_to_check in [player1_won, player2_won]  : 
            # print something .. ?
            print ("Winner found ")
            return True
        pass # End row loop
    
    
    # check cols
    column_to_check = ""
    for col in range(len(board)): # Cols loop        
        for cell in range(len(board[col])) : # Rows loop
            column_to_check += board[cell][col] 
            pass
        if column_to_check in [player1_won, player2_won]  : 
            # print something .. ?
            print ("Winner found ")
            return True            
        
        pass # Cols loop end
     
    # check left diag
    diag_to_check = ""
    for next_cell in range(len(board)):        
        
        """
        . . . .   [0][0]
        x . . .   [1][1]
        0 . . .   [2][2]
        . 0 . x   [3][3]     
        """
        diag_to_check += board[next_cell][next_cell]
        
        pass
    if diag_to_check  in [player1_won, player2_won] : return True
   
    # check right diag     
    diag_to_check = ""
    for next_cell in range(len(board)):       
        
        """
        . . . .   [0][3]     len(board)-next_cell
        x . . .   [1][2]
        0 . . .   [2][1]
        . 0 . x   [3][0]     
        """
        diag_to_check += board[next_cell][len(board)-1-next_cell]        
        pass
    if diag_to_check  in [player1_won, player2_won] : return True    
    return False


current_player = PLAYER_1
moves_counter = 0
game_board = create_game_board()

while not game_over(game_board, moves_counter):
    moves_counter += 1
    print(draw_board(game_board))
    do_next_move(game_board, current_player) # 2 arguments
    # Toogle user
    if current_player == PLAYER_1: current_player = PLAYER_2
    else: current_player = PLAYER_1
    
    pass



print(draw_board(game_board))

print (draw_board(game_board))
