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
    if pile1 > 0: # this is in case there is no pile left when the choice gets to player one
     max_stones = int(input("How many stones do you want to pull" + player + "1-5"))
     if max_stones <= 0:
         max_stones = 0
         print(" stones entered was 0 or a negative")
     if max_stones > 0:
         if max_stones < 6:
          flag = True
          pile1 = pile1 - max_stones
          if pile1 <= 0:
             print("There are no rocks left")
             pile1 = 0
             return
          return
         else:
             print("That is not a number between 1-5")
     else:
      print("That is not a number between 1-5")
    else:
     print("There are", pile1, "rocks left.")
     return
   except ValueError:
     print("That's not a number")
  print(str(pile1) + "in loop")

def stones_game():
  global pile1
  global player
  flag = False
  while flag == False:
   try:
     while flag == False:
      pile = int(input("How large of a pile of stones do you want?"))
      if pile > 1:
       pile1 = pile
       flag = True
      else:
         print("That is not a positive number.")
   except ValueError:
        print("That's not a number")


  while pile1 > 0: #loop that will run until the pile of rocks goes to zero
   flag = False
   player = "player one"
   print(str(player) + " The pile is now " + str(pile1))
   stones(flag, player, pile1)

   player = "player two"
   print(str(player) +" The pile is now " + str(pile1) )
   stones(flag, player, pile1)
  return pile1

global player
stones_game()
print("Game over the winner is " + player )
