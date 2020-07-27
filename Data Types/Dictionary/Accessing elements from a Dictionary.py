#Python program to demonstrate accessing an element from a Dictionary
#Creating a Dictionary
Dict = {1:'Python',2:'with','name':'Pranshu'}

#Accessing an element using Key
print("Accessing an element using key: ")
print(Dict['name'])

#Accessing an element usinh key
print("\nAccessing an element using key: ")
print(Dict[1])

#Accessing an element using get() method
print("\nAccessing an element using get() : ")
print(Dict.get(2))
