#Creating a List
List = ['P','Y','T','H','0','N','W','I','T','H','P','R','A','N','S','H','U']
print("Initial List: ")
print(List)

#Print elements from beginning to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

#Print elements of a range using negative index list slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1: ")
print(Sliced_List)

#Printing elements in reverse using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)