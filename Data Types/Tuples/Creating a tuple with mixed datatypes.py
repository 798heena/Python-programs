#Creating a tuple with Mixed Datatype
Tuple = (5,'Welcome',7,'Pranshu')
print("Tuple with mixed datatypes: ")
print(Tuple)

#Creating a Tuple with nested tuples
Tuple1 = (0,1,2,3)
Tuple2 = ('python','pranshu')
Tuple3 = (Tuple1,Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#Creating a Tuple with repetition
Tuple = ('Python ') * 3
print("\nTuple with repetition: ")
print(Tuple)

#Creating a Tuple with the use of loop
Tuple = ('Pranshu')
n = 5
print("\nTuple with a loop: ")
for i in range(int(n)):
    Tuple = (Tuple,)
    print(Tuple)
