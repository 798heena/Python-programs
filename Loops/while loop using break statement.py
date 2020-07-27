#Python program to demonstrate while loop using break statement

c = 0
while c <= 10:
    print(c)
    c = c+1
    if c == 5:
        break
print('end of loop')