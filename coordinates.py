from random import Random
from string import ascii_uppercase, digits


def get_human_coordinates(board, current_player):
  len_board = len(board)
  uppercases = ascii_uppercase[0:len_board]
  numbers = digits[1:len_board+1]
  user_input = input("Choose your cordinates: ")
  while user_input.lower() != "quit":

    if len(user_input) != 2:
      print("Invalid cordinates. Only 2 characters.")
    else:
      if user_input[0] in uppercases and user_input[1] in numbers:
        row = uppercases.index(user_input[0])
        column = numbers.index(user_input[1])
        if (board[row][column] == "."):
          return (row, column)
        else:
          print("Already taken, try again.")
      else:
        print("Invalid cordinates.Try again")
    user_input = input("Choose your cordinates: ")

  # """
  # Should return the read coordinates for the tic tac toe board from the terminal.
  # The coordinates should be in the format  letter, number where the letter is 
  # A, B or C and the number 1, 2 or 3.
  # If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  # than a warning message should appear and the coordinates reading process repeated.
  # If the user enters a coordinate that is already taken on the board.
  # than a warning message should appear and the coordinates reading process repeated.
  # If the user enters the word "quit" in any format of capitalized letters the program
  # should stop.
  # """

def get_random_ai_coordinates(board): # zwraca losowe wolne indeksy w krotce np: (1, 0)
  import random
  board_lenght = len(board)
  columns = digits[ 0 : board_lenght]
  row = digits[ 0 : board_lenght]
  all_characters_in_list = []
  for i in board:
    all_characters_in_list.extend(i)

  while True:
    computer_coordinate = (int(random.choice(row)), int(random.choice(columns)))

    if board[computer_coordinate[0]][computer_coordinate[1]] == ".":
      return computer_coordinate

    elif "." not in all_characters_in_list:
      return None

    else:
      computer_coordinate = (int(random.choice(row)), int(random.choice(columns)))



def get_unbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 