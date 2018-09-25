

for n in [1.0, 2.0, 3.0, 4, 5, 6, 7, 8, 9, 10]:

       print(1/n)

print(type(n))
float(n)
print(type(n))

n = input("enter number for countdown\n")
while n < 0:
    n = input("enter number for countdown\n")
    if n > 0:
        break
