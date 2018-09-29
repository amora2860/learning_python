# Name: andrew m
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

x = input("please enter a number")

def f1(x):
    print(x + 1)

def f2(x):
    return(x + 1)

print(f1(4))
print(f2(4))
# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####


def rsp(p1, p2):

 if p1 == p2:
   print("Tie")
   return
 elif p1 == "rock" and p2 == "paper":
    print("player 2 wins")
    return

 elif p1 == "rock"and p2 == "scissor":
    print("player 1 wins")
    return

 elif p1 == "scissor" and p2 == "paper":
    print("player one wins")
    return

 elif p1 == "scissor" and p2 == "rock":
    print("player two wins")
    return


 elif p1 == "paper" and p2 == "scissor":
    print("player two wins")
    return

 elif p1 == "paper" and p2 == "rock":
    print("player one wins")
    return
 else:
  print("why would you test for that?")
  return



# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

# 1 test
rsp("rock", "paper")


# 2 test
rsp("paper", "paper")


# 3 test
rsp("paper", "rock")


# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####

# Test cases for not_equal
##### YOUR CODE HERE #####

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####


# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   
