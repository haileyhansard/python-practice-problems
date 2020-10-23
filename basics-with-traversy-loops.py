# A for loop is used for iterating over a sequence (that is either a list, tuple, dictionary, set, or string)

people = ['John', 'Paul', 'Sara', 'Susan']

#Simple For Loop
# for person in people:
#     print(f'Current Person: {person}')

#Break
# for person in people:
#     if person == 'Sara':
#         break
#     print(f'Current Person: {person}')

#Continue (in this example, it will skip Sara and continue on)
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

#Range
for i in range(len(people)):
    print(people[i])

#Custom range (starting and ending index)
for i in range(0, 11):
    print(f'Number: {i}')

#While loops execute a set of statements as long as a condition is true
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1