def requirements():
    print('''1. Lists: mutable, ordered sequence of elements.
2. Lists are mutable - that is, can insert, update, delete.
3. Create lists - using brackets.
4. Create a program that mirrors the following IPO format.
Note: Usere enters the number of requested list elemets, dynamically rendered below (number of elements can change each run)''')
    print()


num = int(input("enter number of list elements: "))
list1 = []
print()

for item in range(num):
    element = input(f'Please enter list elemenet {item+1}: ')
    list1.append(element)
print()    
print('print my list:')
print(list1)
print()

add = input('Please enter list element to be added: ')
position = int(input('At what index would you like to add the element: '))
list1.insert(position, add)
print(list1)

print()
print('Count number of elements in list')
counted = len(list1)
print(counted)

print()
print('Sort the list in alphabetical order')
list1.sort()
print(list1)

print()
print('Reverse the list')
list1.reverse()
print(list1)

print()
print('Remove last list element')
list1.pop()
print(list1)

print()
print('Remove second element of list')
list1.remove(list1[1])
print(list1)

print()
delete_value = input('Pick a value still in the list to delete: ')
if delete_value in list1:
    list1.remove(delete_value)
print(list1)

print()
answer = input('would you like to delete the whole list (y/n): ')
if answer.lower() == 'y':
    list1.clear()
else: print("nothing deleted")
print("this is your deleted list")
print(list1)