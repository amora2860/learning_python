# Name: andrew m
# hw2.py



##### Template for Homework 2, exercises 2.0 - 2.5  ######

import math
import cmath
import random

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
def is_divisible(m, n):

    if m == 0 or n == 0:
        print("cannot divide by 0")
        return
    elif m % n == 0:
        print("True")
        return
    else:
        print("False")
        return

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

is_divisible(10, 5)
    # This should return True
is_divisible(18, 7)  # This should return False

is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####

def not_equal(m, n):
  if m > n:
     print("true")

  elif m < n:
    print("true")

  else:
     print("false")


# Test cases for not_equal
##### YOUR CODE HERE #####
not_equal(5,4)
not_equal(4,4)
not_equal(3,5)


# ********** Exercise 2.3 ********** 
print("excercise 2.3")
## 1 - multadd function
##### YOUR CODE HERE #####
radians = (90.0 / 360.0) * 2 * math.pi
print(math.sin(radians))


## 2 - Equations
##### YOUR CODE HERE #####

# this makes no sense!!!

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
print("Excercise 2.4 random number")

print("#1")
def rand_divis_3():
   a = random.randint(0, 100)
   print(a)
   if (a % 3) == 0:
       print("True")
       return
   else:
       print("False")
       return

rand_divis_3()

print("#2")
b = int(input("How many sides to this dice?"))
c = int(input("How many times do you want to roll?"))

def roll_dice(b, c):

  for i in range(c):
     a = random.randint(1,b)
     print(a)
     c = c - 1
  return

roll_dice(b, c)
print("thats all!")




# ********** Exercise 2.5 **********
print("Exercise 2.5 start")
# code for roots function
##### YOUR CODE HERE #####   

def roots(a,b,c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))


a = float(input("Enter a "))
b = float(input("Enter b "))
c = float(input("Enter c "))
roots(a,b,c)
# Test Cases
##### YOUR CODE HERE #####   
