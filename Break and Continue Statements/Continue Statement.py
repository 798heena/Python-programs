#print odd numbers present in a list
x = [1,2,3,4,5]

for i in x:
    if i % 2 == 0:
        continue
    print(i)
else:
    print("else-block")