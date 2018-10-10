# Name: Andrew
# Section:
# nims.py

# this function it ment to ask the player how many stones do they want in the pile
def ask_pile():
  global pile1
  try:
     pile = int(input("How large of a pile of stones do you want?"))
     pile1 = pile
     if pile < 1:
      return pile, pile1
  except ValueError:
     print("That's not a number")

def stones(flag, player, pile):
  global pile1
  while flag != True: #players turn starts
   try:
    print(str(pile1) + "inside of stones")
    if pile1 > 0: # this is in case there is no pile left when the choice gets to player one
     max_stones = int(input("How many stones do you want to pull" + player + "1-5"))
     if max_stones <= 0:
         max_stones = 0
         print(" stones entered was 0 or a negative")
     if max_stones == 5 or 4 or 3 or 2 or 1:
         flag = True
         pile1 = pile1 - max_stones
         if pile1 <= 0:
             print("There are no rocks left")
             pile1 = 0
             return
         print(str(pile1) + "leaving stones")
         return
     else:
         print("That is not a number between 1-5")
    else:
      print("There are", pile1, "rocks left.")
    print(max_stones)
   except ValueError:
     print("That's not a number")
  print(str(pile1) + "in loop")

def stones_game():
  global pile1
  global player
  try:
    pile = int(input("How large of a pile of stones do you want?"))
    if pile > 1:
     pile1 = pile

  except ValueError:
        print("That's not a number")

  flag = False  # this flag is used to keep track of correct responses
  print(str(pile) + "begining of stones_game")
  while pile1 > 0: #loop that will run until the pile of rocks goes to zero
   flag = False
   player = "player one"
   print(str(pile1) + " before stones player one")
   stones(flag, player, pile1)
   print(str(pile1) + " pile1 value")
   player = "player two"
   print(str(pile1) + " before player two")
   stones(flag, player, pile1)
  return pile1

global player
stones_game()
print("Game over the winner is " + player )
