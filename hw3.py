# Name: Andrew M.
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 


# Define your function here
def list_intersection(a,b):
 c = set(a) & set(b)

 return c

print(list_intersection([1,2,3,4,6,2,3], [3,1,5,8,6,7,5,3,2]))


# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    from math import sqrt
    ##### YOUR CODE HERE #####
  # calculate the distance between the centers
    x1 = ball1[0]
    x2 = ball2[0]
    y1 = ball1[1]
    y2 = ball2[1]
    r1 = ball1[2]
    r2 = ball2[2]

    distance_between_centers =  sqrt(((x2-x1)**2)+((y2 - y1)**2))
    total_radius_distance = r1 + r2
    if distance_between_centers <= total_radius_distance:
        print("this is the distance between the centers" + str(distance_between_centers))
        print("total radius added" + str(total_radius_distance))
        print("this is the value of X1 " + str(x1))
        print("this is the value of X2 " + str(x2))
        print("this is the value of y1 " + str(y1))
        print("this is the value of y2 " + str(y2))
        return True
    else:
     print("this is the distance between the centers" +str(distance_between_centers))
     print("this is the distance of the radius" + str(total_radius_distance))
     return False

    #if distance is less than or equal to radius


# Test Cases for Exercise 3.2
print(ball_collide((0, 0, 1), (3, 3, 1))) # Should be False
print(ball_collide((5, 5, 2), (2, 8, 3))) # Should be True
print(ball_collide((7, 8, 2), (4, 4, 3))) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term

my_classes = {}


def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    global my_classes
    my_classes.update({class_num : desc})
    return

# Here, use add_class to add the classes you're taking next term
add_class("6.189", "Introduction to Python")
add_class("6.876", "iuytrt")
add_class("6.189", "Introduction to Python")

def print_classes(course):
    ##### YOUR CODE HERE #####
    if course in my_classes.keys():
     print(course + " - " + str(my_classes.get(course)))
     return
    else:
        print("No courses " + str(course) + "classes taken")

    return "Not Yet Implemented"

# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
print_classes("6.189")
print_classes("6.6")
print_classes("6.876")
# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank','Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

comb_dict = {}

# Define your functions here
def combine_lists():
    global comb_dict
    global NAMES
    global AGES

    i = 0

    while i < len(AGES):

     comb_dict.update({NAMES[i]: AGES[i]})
     i = i + 1
     print()
    return

def people(age):
    # Use combined_dict within this function...
    global comb_dict
    i = 1
    for k,v in comb_dict.items():

     i= i +1
     if age == v:
      print(k)
    return

combine_lists()

# Test Cases for Exercise 3.4 (all should be True)
print(people(18))
print(people(21) ==   ['Bob'])
print(people(22) ==   ['Kelly'])
print(people(23) ==   [])

# **********  Exercise 3.5 **********

import calendar

print()

def zellers(month, day, year):
    day = calendar.weekday(year, month, day)
    if day == 0:
     print("monday")
    elif day == 1:
      print("Tuesday")
    elif day == 2:
      print("Wednesday")
    elif day == 3:
      print("Thurday")
    elif day == 4:
      print("friday")
    elif day == 5:
      print("saturday")
    elif day == 6:
      print("sunday")
    return

# Test Cases for Exercise 3.5
#print zellers("March", 10, 1940) == "Sunday" # This should be True
##### YOUR CODE HERE #####
zellers(3,10,1940)
zellers(6,15,1976)