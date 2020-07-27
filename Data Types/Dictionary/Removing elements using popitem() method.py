#Creating Dictionary
Dict = {1:'Python',2:'with','name':'Pranshu'}

#Deleting an arbitrary key using popitem() function
pop_ele = Dict.popitem()
print("Dictionary after deletion: " + str(Dict))
print("\nThe arbitrary pair returned is: " + str(pop_ele))