#TUPLES
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

#Create tuple with a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#single value in a tuple needs a trailing comma
fruits3 = ('Mango',)

print(fruits, fruits2)
print(fruits3, type(fruits3))

#Get a value
print(fruits[1])

#Can't change the value
# fruits[0] = 'Pears' ##will have type error bc tuples cannot be changed

#Delete
del fruits2

#Get length
print(len(fruits))

#SETS

#A set is a collection which is unordered and unindexed. No duplicate members.

#Create a set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

#Check if in set
print('Apples' in fruits_set) #returns True because apples is in the fruits_set

fruits_set.add('Grapes')

fruits_set.remove('Mangoes')

print(fruits_set)