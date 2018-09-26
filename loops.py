
#1.8 #1
for n in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:

       print(1/n)
#-----------------------------------------------------------------------------------------------
#1.8 #2

# found this try and catch code which is nice to eliminate out bad inputs.
while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        n = int(input("enter number for countdown\n"))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break


b = int(n)

while b <= 0:
    n = input("enter a positive number for countdown\n")
    b = int(n)
    if b >= 0:
        break
while b > 0:
    b -= 1
    if b == 0:
        print(b)
        break
    print(b)

#-------------------------------------------------------------------------------

#1.8 #3

base = int(input("enter base"))
exp = int(input("enter exponent"))

print(base**exp)
