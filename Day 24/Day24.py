# one way to open file and read what is inside or write in it

""" file = open("myFile.txt")
contents = file.read()
print(contents)
file.close() """

"""
There are modes used while opening file
"r": means read only and it is the default
"w": means to overwrite on the file and save it if file doesnt exist it will write a new one
"a": means append the string we writing to the found string
Hello, my name is Aboud
"""

# another way that open file and close as soon as we are finished with the file
with open("/Users/youse/myFile.txt") as f:
    contents = f.read()
    print(contents)

# to write to file without delete prevoius
""" with open("myFile.txt",mode='a') as f:
    f.write('\nHello AHMED') """