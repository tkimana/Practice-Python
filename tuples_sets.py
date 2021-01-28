# A Tuple is a collection which is ordered and unchangeble. Allows duplicate members


# Create a tuples

fruits= ('apples', 'oranges', 'grapes')
fruits2=tuple(('apples', 'oranges', 'grapes'))

# Single value needs trailing comma

fruits2= ('apples')

# Can't Change a tuple

#fruits[0]='banana'

#Delete a tuple

del fruits2

# Get length

print(len(fruits))

#print(fruits2)

# A set is a collection which is unordered unidexed. No duplicate members

# Create a set 

fruits_sets= {'apples', 'grapes', 'oranges'}

# Check if in set

print('oranges' in fruits_sets)

# Add to set 

fruits_sets.add('banana')


# Add duplicate set

fruits_sets.add('banana')

print(fruits_sets)

# Remove the set 

fruits_sets.remove('apples')

# Clear the set 

fruits_sets.clear()

# Delete the set 

del fruits_sets


print(fruits_sets)