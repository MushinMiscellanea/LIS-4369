def requirements():
    print('''1. Run this tuple stuff
2. cannot use list functions like append, replace, split on tuples (obv)
3. Do the stuff you can do with tuples''')

tuple1= ('Deadmanu5', 'Noisia', 'Tame Impala', 'Division By Zero')
tuple2= 666, 'pyfun', 64.00, 'RAM'

print('Print tuple1')
print(tuple1)
print()

print('Print tuple2')
print(tuple2)
print()

mau5, atom, currents, me = tuple1
print('tuple1 unpacking')
print(f'{mau5} {atom} {currents} {me}')
print()

print('Print 3rd element in tuple2 (64.00)')
print(tuple2[2])
print()

print('Print slice of tuple (second and third element)')
print(tuple2[1:3])
print()

print('reasign tuple2 using parenthesis')
tuple2 = (1,2,3,4)
'''tuple_to_list = list(tuple2)
for item in tuple_to_list[2:]:
    tuple_to_list.remove(item)
tuple_to_list.append('adding')
tuple_to_list.append('this')
list_to_tuple = tuple(tuple_to_list)'''
print(tuple2)
print()

print('Reasign tuple2 using packing')
tuple2 = 'one', 'two', 'three', 'four'
'''tuple2 = list(tuple2)
tuple2.clear()
tuple2 = 1, 2, 'repacking', 'tuple'
tuple2 = tuple(tuple2)'''
print(tuple2)
print()

print('number of elements in tuple1:',len(tuple1))
print()
print('Print the type of tuple1:', type(tuple1))


