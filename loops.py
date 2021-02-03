# A for loop is used for iterating over a sequence (that s either a list, a tuple, a dictionary, a set, or a string).

people = ['john', 'james', 'greg', 'susan']

# Simple for loop

#for person in people:
    #print(f'Current person: {person}')


# Use Break 
for person in people:
    if person=='greg':
        break
    print(f'Current person:{person}')


# Use Continue

for i in people:
    if i=='greg':
        continue
    print(f'Current person1:{i}')

# use range

for i in range(len(people)):
    print(people[i])


for i in range(0, 100):
    print(i)

# While loops execute a set of statements as long as condition is true

count= 0
while count <=10:
    print(f'Number: {count}')
    count +=1


