# Name: Andrew M.
# Section:
# nims.py



'''
while flag != True : #Ensures that the loop is not exited until everything is satifies.
 while pile < 1:
  try:
    pile = int(input("How large of a pile of stones do you want?"))
    flag = True
  except ValueError:
    print("That's not a number")

flag = False #this ensures that the loop to ask player one for how many stones is entered.
'''
def ask_pile():
  try:
    pile = int(input("How large of a pile of stones do you want?"))
    if pile < 1:
     return pile
  except ValueError:
    print("That's not a number")



def stones(flag, player,pile):
 while flag != True: #players turn starts
  try:
   if pile > 0: # this is in case there is no pile left when the choice gets to player one
    max_stones = int(input("How many stones do you want to pull" + player + "1-5"))
    pile = pile - max_stones
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
 return

def stones_game():
 flag = False  # this flag is used to keep track of correct responses
 pile = 0
 ask_pile()
 while pile > 0: #loop that will run until the pile of rocks goes to zero
  flag = False
  player = "player one"
  stones(flag,player,pile)
  player = "player two"
  print(pile)
  stones(flag,player,pile)
 return

stones_game()


 # player ones turn starts
'''while flag != True: 
  try:
   if pile > 0: # this is in case there is no pile left when the choice gets to player one
    max_stones = int(input("How many stones do you want to pull Player one 1-5?"))
    pile = pile - max_stones
    winner = "Player one"
    if pile <= 0:
     print("There are no rocks left")
    else:
     print("There are", pile, "rocks left.")
   if max_stones == 1 or 2 or 3 or 4 or 5:
    flag = True
   else:
     print("That is not a number between 1-5")
  except ValueError:
    print("That's not a number")
'''
#player two turn starts
''' flag = False
 while flag != True:

  try:
   if pile > 0:
    max_stones = int(input("How many stones do you want to pull Player two 1-5?"))
    pile = pile - max_stones
    winner = "Player Two"
    if pile <= 0:
     print("There are no rocks left")
    else:
     print("There are", pile, "rocks left.")
   if max_stones == 1 or 2 or 3 or 4 or 5:
    flag = True
   else:
    print("That is not a number between 1-5")
  except ValueError:
   print("That's not a number") 
'''

print("Game over the winner is ")
