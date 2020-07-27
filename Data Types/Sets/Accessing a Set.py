#Python program to demonstrate Accessing of elements in a Set
#Creating a Set
set1 = set(["Python","with","Pranshu"])
print("\nInitial set: ")
print(set1)

#Accessing elements using for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")

#Checking the element using in keyword
print("Pranshu" in set1)