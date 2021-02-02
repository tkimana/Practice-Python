# A for loop is used for iterating over a sequence (that s either a list, a tuple, a dictionary, a set, or a string).

people = ['john', 'james', 'greg', 'susan']

# Simple for loop

#for person in people:
    #print(f'Current person: {person}')


# Use Break 
for person in people:
    if person=='susan':
        break
    print(f'Current person:{person}')