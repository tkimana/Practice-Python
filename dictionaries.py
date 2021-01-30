# A Dictionaries is a collection which is unordered, changeable and indexed. No duplicate members.

#Note: Dictionaries are same as Objects in javascipt 

#Create dict
person={
'first_name' : 'theodore',
'last_name' : 'kimana',
'age': 24,
}

household={
  'dad': 'Theobare',
  'mom' : 'Odette',
  'dad_age': 54,
  'mom_age': 40,
}

# Use Constractor
person2= dict(first_name='Sara', last_name='james')

# Get a Value in dict

print(household['mom'])
print(person.get('last_name'))

# Add key/value

person['phone']='200000'

# Get dict keys

print(person.keys())

# Get dict value

print(person.values())

#print(person)

# Get dict items

print(person.items())

# Copy dict
household=person.copy()
household['city']= 'Boston'

# Remove item

del(household['city'])

print(household)

del (person['first_name'])

print(person)

# Clear 

person.clear()

print(person)

# Length in dictionaries

print(len(household))

person.pop('phone')

print(person)
#print(household)

# Clear

household.clear()

print(household)



#print(person2, type(person2))