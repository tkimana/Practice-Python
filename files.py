# Python has functions for creating, reading, updating and deleting files.


# Open a file

myFile= open('myfile.txt', 'w')

# Get some info
print('Name:', myFile.name)
print('Is Closed:', myFile.closed)
print('Opening Mod:', myFile.mode)

# Write to file

myFile.write('I like py')
myFile.write(' and Java')
myFile.close()


# Append to file

myFile= open('myfile.txt', 'a')
myFile.write(' I also like javascript')
myFile.close()

# Read from a file

myFile= open('myfile.txt', 'r+')
text= myFile.read(100)
print(text)