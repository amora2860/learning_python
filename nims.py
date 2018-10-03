# Name:
# Section:
# nims.py

flag = False #this flag is used to keep track of correct responses
pile = 0

while flag != True : #Ensures that the loop is not exited until everything is satifies.
 while pile < 1:
  try:
    pile = int(input("How large of a pile of stones do you want?"))
    flag = True
  except ValueError:
    print("That's not a number")

flag = False #this ensures that the loop to ask player one for how many stones is entered.


while pile > 0: #loop that will run until the pile of rocks goes to zero
 flag = False

 while flag != True: #player ones turn starts
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

#player two turn starts
 flag = False
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

print("Game over the winner is ", winner)
