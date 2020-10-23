#Python String Methods
s = 'hello world'
print(s.capitalize())
print(s.upper())
print(len(s))
print(s.replace('world', 'everyone'))

#F string
print(f'Translate this phrase to Spanish: {s}')

#LISTS
#Similar to arrays in JS. 
#A collection which is ordered and changeable. Allows duplicate members.

#Create a list (Most common way)
numbers = [1, 2, 3, 4, 5]

#Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

#Working with a list
fruits = ['apples', 'oranges', 'grapes', 'pears']

#Get a value
print(fruits[1])

#Get length of list
print(len(fruits))

#Append to list
fruits.append('mangos')

#Remove from list
fruits.remove('grapes')

#Insert into specific postion - pass in the position and the value
fruits.insert(2, 'strawberries')

#Remove from certain position with POP
fruits.pop(2)

#Reverse the list
fruits.reverse()

#Sort alphabetically
fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

#Change a value
fruits[0] = 'blueberries'

print(fruits)