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
flag = False

while flag != True:

 try:
  pile = int(input("How large of a pile of stones do you want?"))
  flag = True
 except ValueError:
   print("That's not a number")

flag = False

while flag != True:

 try:
  max_stones = int(input("How many stones do you want to pull 1-5?"))

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
