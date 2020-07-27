#Python Program showing how to take
#multiple input using split

#taking two inputs at a time
x,y = input("Enter two values: ").split()
print("Number of boys: ",x)
print("number of girls: ",y)
print()

#taking three inputs at a time
x,y,z = input("Enter three values: ").split()
print("Number of boys: ",x)
print("number of girls: ",y)
print("total number of students: ",z)
print()

#taking two inputs at a time
a,b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a,b))
print()

#taking multiple inputs at a time
#type casting using list() function
x = list((map(int,input("Enter multiple values: ").split())))
print("List of Students: ",x)