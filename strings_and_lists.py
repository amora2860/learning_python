# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
#print("sum_all of [4, 3, 6] is:", sum_all([4, 3, 6]))
#print("sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4]))


def cumulative_sum(number_list):
    # number_list is a list of numbers
    cumul_total = []
    flag = True # Ensures that the first value is entered unchanged into the list.
    for i in number_list:

     if flag == True:
       # dont add 4 to its self
      print(i)
      cumul_total.append(i)
      flag = False #makes sure we do not enter this again
      n = i
     else:

      n += i # add the previous number in the list to the next number
      print(n)
      cumul_total.append(n)
      n = i
    return cumul_total

#print("The cumulative sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6]))
#print("This is the end of Exercise 2.7")

# **********  Exercise 2.8 **********

def report_card():

#ask for class name and the gpa
 done = "no"
 gpa = []
 class_list = []
 try:
  while done != "yes":
   gpas = int(input("what was your GPA?"))
   gpa.append(gpas)
   classes = str(input("what is the class name?")) # list one has names of the classes
   class_list.append(classes)
   response = str(input("Are you done? yes or no"))    #ask if there are more classes to enter and to enter y or n
   if response == "yes":
       done = "yes"
 except ValueError:
     print("That's not a number")

 print(gpa)
 print(class_list)
 for i in range(len(gpa)):
  print(str(gpa[i]) + " - " + str(class_list[i]))
 print("Overall GPA   " +  str(sum(gpa)/len(gpa)))





#take the total of the GPA list and divide by the total number of items in either list
#x = len(gpa)
#print(sum of gpa() / x)

#report_card()

    
#
# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********





# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    list = []
    a = word
    list = a
    # word is a string to convert to pig-latin
    list2 = list[0] # this grabs just the first letter of the word.
    list3 = list[1:]#this will grab everything but the first letter of the word.

    for i in VOWELS:
     if list2 == i:
      list = list + "hay"
      print(list)
      return
    list4 = list3 + list2 + "ay"
    print(list4)
    return "Not Implemented Yet"

pig_latin("pig")
pig_latin("are")

# **********  Exercise 2.10 **********

#1
#Print out a list that is cubed using list comprehesion
list = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
cubed_ints = [ e**3 for e in list]
print(cubed_ints)
#2
#skipping lame
#3
list2 = input("type in a word")
vowels = "aeiou"
vowels_in_word = [i for i in list2 if i in vowels]
print(len(list2))
print(vowels_in_word)

#4
listx = [10,20,30]
listy = [1,2,3]
listxy = [x+y for x in listx for y in listy]
print(listxy)