import tic_tac_toe_v4_utils as game

current_player = game.PLAYER_1
moves_counter = 0
game_board = game.create_game_board()

while not game.game_over(game_board, moves_counter):
    moves_counter += 1
    print(game.draw_board(game_board))
    game.do_next_move(game_board, current_player) # 2 arguments
    # Toogle user
    if current_player == game.PLAYER_1: current_player = game.PLAYER_2
    else: current_player = game.PLAYER_1
    
    pass



print(game.draw_board(game_board))

print (game.draw_board(game_board))
