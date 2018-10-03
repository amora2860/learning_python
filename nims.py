# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''



    ## Basic structure of program (feel free to alter as you please):
#this flag is used to keep track of correct responses
flag = False


while flag != True:

 try:
  pile = int(input("How large of a pile of stones do you want?"))
  flag = True
 except ValueError:
   print("That's not a number")

flag = False #this ensures that the loop to ask player one for how many stones is entered.

print("the amount of rocks remaining is", pile)
while pile > 0: #loop that will run until the pile of rocks goes to zero
  flag = False
 while flag != True:
#player ones turn starts
  try:
   max_stones = int(input("How many stones do you want to pull Player one 1-5?"))
   pile = pile - max_stones
   print("the amount of rocks left is", pile)
   winner = "Player one"
   if pile <=0:
       print(winner)
   if max_stones == 1 or 2 or 3 or 4 or 5:
    flag = True
   else:
    print("That is not a number between 1-5")
  except ValueError:
   print("That's not a number")

#player two turn starts
 print("the amount of rocks remaining is", pile)
 flag = False
 while flag != True:

  try:
   max_stones = int(input("How many stones do you want to pull Player two 1-5?"))
   pile = pile - max_stones
   print("the amount of rocks left is", pile)
   if max_stones == 1 or 2 or 3 or 4 or 5:
    flag = True
   else:
    print("That is not a number between 1-5")
  except ValueError:
   print("That's not a number")



#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"
