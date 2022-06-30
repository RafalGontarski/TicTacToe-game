from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option
import random


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():

    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = random.choice(["X","O"])

    if game_mode == 1: #human vs human
        while is_game_running:
            display_board(board)
            if current_player == "X":
                x,y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                current_player = "O"
                #x,y = get_random_ai_coordinates(board)
                
            else:
                #x,y = get_human_coordinates(board, current_player)
                x,y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                current_player = "X"
                
            winning_player = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if its_a_tie and winning_player == None:
                display_board(board)
                print("It's a tie!")
                break
            elif winning_player != None:
                display_board(board)
                print("The game has end.", winning_player, " has won.")
                break

    elif game_mode == 2:
        while is_game_running:
            display_board(board)
            if current_player == "X":
                x,y = get_random_ai_coordinates(board)
                board[x][y] = current_player
                current_player = "O"
                input()
                #x,y = get_random_ai_coordinates(board)
                
            else:
                #x,y = get_human_coordinates(board, current_player)
                x,y = get_random_ai_coordinates(board)
                board[x][y] = current_player
                current_player = "X"
                input()
                
            winning_player = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if its_a_tie and winning_player == None:
                display_board(board)
                print("It's a tie!")
                break
            elif winning_player != None:
                display_board(board)
                print("The game has end.", winning_player, " has won.")
                break


    elif game_mode == 3:
        while is_game_running:
            display_board(board)
            
            ### TO DO ###
            # in each new iteration of the while loop the program should 
            # alternate the value of `current_player` from `X` to `O`
            if current_player == "X":
                x,y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                current_player = "O"
                #x,y = get_random_ai_coordinates(board)
                
            else:
                #x,y = get_human_coordinates(board, current_player)
                x,y = get_random_ai_coordinates(board)
                board[x][y] = current_player
                current_player = "X"
                
            winning_player = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if its_a_tie and winning_player == None:
                display_board(board)
                print("It's a tie!")
                break
            elif winning_player != None:
                display_board(board)
                print("The game has end.", winning_player, " has won.")
                break
            
    elif game_mode == 4:
        print("Still in progress mate.Maybe soon :D")



        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates
        #x,y = get_human_coordinates(board, current_player)
        #x,y = get_random_ai_coordinates(board)

        #board[x][y] = current_player
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
      
if __name__ == "__main__":
    main()