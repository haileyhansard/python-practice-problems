#A dictionary is a collection which is unordered, changeable, and indexed. No duplicate members.
#similar to an object in JS.

#Create a dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 37
}

#Use a constructor

person2 = dict(first_name="Sara", last_name="Williams")
print(person, type(person))
print(person2, type(person2))

#Get value
print(person['first_name'])
print(person.get('last_name'))

#Add key/value
person['phone'] = '555-555-5555'

#Get dictionary keys
print(person.keys())

#Get dictionary items
print(person.items())

#Copy dict (similar to spread operator)
person3 = person.copy()
person3['city'] = 'Boston'

print(person3)

#Remove at item
del(person['age'])

person.pop('phone')

#Clear - now the dict will be empty
person.clear()

#Get length
print(len(person3))

#print(person)

#List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])