# If/Else conditions are used to decide to do something based on something being true or false

x=10
y=10

# Comparison Operators (==, !=, >, <, >= , <=) - Used to compare values

# If/else statement

#if x > y:
    #print(f'{x} is greater than {y}')

#else: 
    #print(f'{y} is greater than {x}')

# elif

#if x > y:
    #print(f'{x} is greater than {y}')

#elif x == y: 
    #print(f'{x} is equal to {y}')

#else: 
    #print(f'{y} is greater than {x}')


# Nested if statement 

#if x> 2:
    #if x <=2:
        #print(f'{x} is greater than 2 and less than or equal to 10')


 # Membership Operators (not, not in) - Membership operators are used to test if sequence is presented in an object 
#if x> 2:
    #if x <= 10:
        #print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# AND
#if x > 2 and x<=10:
    #print(f'{x} is greater than 2 and less than or equal to 10')

# OR
#if x > 2 or x<=10:
    #print(f'{x} is greater than 2 or less than or equal to 10')

# NOT


# Membership Operators (not, not in) - Membership operators are used to test if sequence is presented in an object 


numbers = [1,2,3,4,5]

# IN 
if x in numbers:
    print(x in numbers)

# NOT IN 
if x not in numbers:
    print(x not in numbers)

# Identify Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the memory location:


# IS 

if x is y:
    print(x is y)

# NOT 
if x is not y:
    print(x is not y)
