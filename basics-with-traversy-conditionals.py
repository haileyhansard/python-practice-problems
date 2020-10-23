#If/Else conditions are used to decide to do something based on something being true or false

x = 10
y = 2
z = 7

#Comparison operators ==, !=, >, <, >=, <=
#Used to compare values

#Simple If
if x > y:
    print(f'{x} is greater than {y}')

#If/Else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')


#Elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

#Nested If
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

#Cleaner way of doing that:
if x > 2 and x <= 11:
    print(f'{x} is greater than 2 and less than or equal to 11')


#Logical operators and, or, not
#Used to combine conditional statements

#Membership operators (in, not in )
#Used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

# in 
if z in numbers:
    print(z in numbers)

#not in
if z not in numbers:
    print(z not in numbers)

