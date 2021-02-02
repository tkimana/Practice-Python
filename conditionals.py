# If/Else conditions are used to decide to do something based on something being true or false

x=3
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
if x> 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# AND
if x > 2 and x<=10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# OR
if x > 2 or x<=10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# NOT

if not(x==y):
    print(f'{x} is not equal to {y}')


numbers = [1,2,4,5,6]
if x in numbers:
    print(x in numbers)
