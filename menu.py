from string import digits
from shared import check_input

def get_menu_option():
  # 1 - Lista
  menu_options = [
    "Human vs Human",
    "Random AI vs Random AI",
    "Human vs Random AI",
    "Human vs Unbeatable AI"
  ]
  for i in range(len(menu_options)):
    print(f"{i+1}.", menu_options[i])
    #print(str(i+1) + ". " + menu_options[i])

  choose_range = digits[1:len(menu_options)+1]
  #print(digits[1:len(menu_options)+1])
  # 2 - Słownik
  # user_choose =	{
  #   1: "Human vs Human",
  #   2: "Random AI vs Random AI",
  #   3: "Human vs Random AI",
  #   4: "Human vs Unbeatable AI"
  # }

  # for key, value in user_choose.items():
  #   print(f"{key}.", value)
  
  user_input = input("Choose an option: ")
  check_input(user_input)

  while user_input not in choose_range:
    print("Try again")
    user_input = input("Choose an option: ")
    check_input(user_input)

  return int(user_input)

  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option) 