#Initial Dictionary
Dict = {5:'Pranshu',6:'Welcomes',7:'You','A':{1:'Python',2:'with',3:'Pranshu'},'B':{1:'Python',2:'World'}}
print("Initial Dictionary: ")
print(Dict)

#Deleting a Key Value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

#Deleting a Key from Nested Dictionary'
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)