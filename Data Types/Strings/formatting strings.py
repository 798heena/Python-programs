#Python Program for Formatting of Strings
#Default Order
String = "{} {} {}".format('Python','with','Pranshu')
print("Print string in default order: ")
print(String)

#Positional Formatting
String = "{1} {0} {2}".format('Python','with','Pranshu')
print("\nPrint string in positional order: ")
print(String)

#Keyword Formatting
String = "{p} {w} {h}".format(p = 'Python',w = 'with',h = 'Pranshu')
print("\nPrint string in positional order: ")
print(String)

#Formatting of Integers
String = "{0:b}".format(16)
print("\nBinary representation of 16: ")
print(String)

#Formatting of Floats
String = "{0:e}".format(165.6458)
print("\nExponent Representation of 165.6458: ")
print(String)

#Rounding off Integers
String = "{0:.2f}".format(1/6)
print("\none-sixth: ")
print(String)