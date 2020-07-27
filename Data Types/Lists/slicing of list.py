#Python program to demonstrate removal of elements in a List
#Creating a List
List = ['P','Y','T','H','0','N','W','I','T','H','P','R','A','N','S','H','U']
print("Initial List: ")
print(List)

#Print elements from a range using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

#Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th element till the end: ")
print(Sliced_List)

#Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)