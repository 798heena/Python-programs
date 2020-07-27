#Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

#Adding elements one at a time
Dict[0] = 'Python'
Dict[2] = 'with'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

#Adding set of values to a single key
Dict['Value_set'] = 2,3,4
print("\nDictionary after adding 3 elements: ")
print(Dict)

#Updating existing Keys's Value
Dict[2] = 'Welcome'
print("\nUpdated Key Value: ")
print(Dict)

#Adding Nested Key Value to Dictionary
Dict[5] = {'Nested':{'1':'Life','2':'Pranshu'}}
print("\nAdding a Nested Key: ")
print(Dict)