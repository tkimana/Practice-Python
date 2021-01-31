# If/Else conditions are used to decide to do something based on something being true or false


x=10
y=10

# Comparison Operators (==, !=, >, <, >= , <=) - Used to compare values


# If/else statement

if x > y:
    print(f'{x} is greater than {y}')

else: 
    print(f'{y} is greater than {x}')


# elif

if x > y:
    print(f'{x} is greater than {y}')

elif x == y: 
    print(f'{x} is equal to {y}')

else: 
    print(f'{y} is greater than {x}')


# Nested if statement 

if x> 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x<=10:
    print(f'{x} is greater than 2 and less than or equal to 10')



