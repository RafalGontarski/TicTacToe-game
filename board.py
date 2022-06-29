from string import ascii_uppercase, digits


def get_empty_board():
  board = [['.', '.', '.',], ['.', '.', '.',], ['.', '.', '.',]]
  return board

def display_board(board):

  board_len = len(board)
  line = ["---"]
  add_line = "+".join(line * board_len)
  main_line = ("  " + (add_line))

  print("   " + "   ".join(digits[1:board_len + 1]))
  
  for i in range(board_len):
    print(ascii_uppercase[i]+"  " + " | ".join(board[i]))
    if i == board_len - 1:
      continue
    print(main_line)

board = get_empty_board()
display_board(board)

def is_board_full(board):  # zwraca true lub false

  all_characters_in_board = []
  for i in board:
    all_characters_in_board.extend(i)

  if "." in all_characters_in_board:
    return True
  else:
    return False

# should return True if there are no more empty place on the board,
# otherwise should return False
  


def get_winning_player(board):  # zwraca 'o' albo 'x'
  board_lenght = len(board)

  for row in range(board_lenght):
    if (board[row][0] + board[row][1] + board[row][2]) == "xxx":
      return 'x'
  for row in range(board_lenght):
    if (board[row][0] + board[row][1] + board[row][2]) == "ooo":
      return 'o'
  
  for column in range(board_lenght):
    if (board[0][column] + board[1][column] + board[2][column]) == "xxx":
      return 'x'
  for column in range(board_lenght):
    if (board[0][column] + board[1][column] + board[2][column]) == "ooo":
      return 'o'
  
  if (board[0][0] + board [1][1] + board[2][2]) == "xxx":
    return 'x'
  if (board[0][0] + board [1][1] + board[2][2]) == "ooo":
    return 'o'

  if (board[0][2] + board [1][1] + board[2][0]) == "xxx":
    return 'x'
  if (board[0][2] + board [1][1] + board[2][0]) == "ooo":
    return 'o'
#   """
#   Should return the player that wins based on the tic tac toe rules.
#   If no player has won, than "None" is returned.
#   """
#   pass


# # run this file to test whether you have correctly implemented the functions
# if __name__ == "__main__":
#     empty_board = get_empty_board()
#     print(empty_board)

#     board = [
#       ['X', "O", "."],
#       ['X', "O", "."]
#       ['0', "X", "."]
#     ]
#     print("""
#     should print 
#         1   2   3
#     A   X | O | . 
#        ---+---+---
#     B   X | O | .
#        ---+---+---
#     C   0 | X | . 
#        ---+---+---
#     """)
    
#     display_board(board)
    
#     board_1 = [
#       ["X", "O", "."],
#       ["X", "O", "."],
#       ["X", "X", "O"],
#     ]
#     print("Should return False")
#     print(is_board_full(board_1)) 

#     board_2 = [
#       [".", "O", "O"],
#       [".", "O", "X"],
#       [".", "X", "X"],
#     ]
#     print("Should return False")
#     print(is_board_full(board_2)) 

#     board_3 = [
#       ["O", "O", "X"],
#       ["O", "X", "O"],
#       ["O", "X", "X"],
#     ]
#     print("Should return True")
#     print(is_board_full(board_3)) 

#     board_4 = [
#       ["X", "O", "."],
#       ["X", "O", "."],
#       ["X", "X", "O"],
#     ]
#     print("Should return X")
#     print(get_winning_player(board_4))

#     board_5 = [
#       ["X", "O", "O"],
#       ["X", "O", "."],
#       ["O", "X", "X"],
#     ]
#     print("Should return O")
#     print(get_winning_player(board_5))

#     board_6 = [
#       ["O", "O", "."],
#       ["O", "X", "."],
#       [".", "X", "."],
#     ]
#     print("Should return None")
#     print(get_winning_player(board_6))