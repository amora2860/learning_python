# Name: Andrew M.
# Section:
# nims.py



def ask_pile():
  global pile
  try:
     pile = int(input("How large of a pile of stones do you want?"))
     if pile < 1:
      return pile
  except ValueError:
     print("That's not a number")

def stones(flag, player, pile):
  global max_stones
  while flag != True: #players turn starts
   try:
    if pile > 0: # this is in case there is no pile left when the choice gets to player one
     max_stones = int(input("How many stones do you want to pull" + player + "1-5"))
     pile = pile - max_stones
     print(pile)
     if pile <= 0:
      print("There are no rocks left")
     else:
      print("There are", pile, "rocks left.")
    if max_stones == 1 or 2 or 3 or 4 or 5:
     flag = True
     return
    else:
      print("That is not a number between 1-5")
   except ValueError:
     print("That's not a number")
  print(str(pile) + "in loop")
  return pile, max_stones

def stones_game():
  global pile
  flag = False  # this flag is used to keep track of correct responses
  print(pile)
  while pile > 0: #loop that will run until the pile of rocks goes to zero
   flag = False
   player = "player one"
   stones(flag, player, pile)
   player = "player two"
   print(pile)
   stones(flag, player, pile)
  return

def stones(flag, player, pile):
  global max_stones
  while flag != True: #players turn starts
   try:
    if pile > 0: # this is in case there is no pile left when the choice gets to player one
     max_stones = int(input("How many stones do you want to pull" + player + "1-5"))
     pile = pile - max_stones
     print(pile)
     if pile <= 0:
      print("There are no rocks left")
     else:
      print("There are", pile, "rocks left.")
    if max_stones == 1 or 2 or 3 or 4 or 5:
     flag = True
     return
    else:
      print("That is not a number between 1-5")
   except ValueError:
     print("That's not a number")
  print(str(pile) + "in loop")
  return pile, max_stones


ask_pile()
stones_game()
print("Game over the winner is ")
