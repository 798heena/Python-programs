#Python program showing
#how to take multiple input
#using list comprehend

#taking two input at a time
x,y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ",x)
print("Second Number is: ",y)
print()

#taking three inputs at a time
x,y,z = [int(x) for x in input("Enter three values: ".split())]
print("First Number is: ",x)
print("Second Number is: ",y)
print("Third Number is: ",z)
print()

#taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list are: ",x)