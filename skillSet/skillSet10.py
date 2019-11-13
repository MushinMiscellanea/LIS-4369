def requirements():
    print('''1. Dictionaries (Python data set): undordered key:value pairs.
2. Dictionary: an associative array (also known as hashes).
3. Any key in a dictionary is associated to a value.
4. Keys: must be of immutable type (string, number or tuple with immutable elements and must be unique).
Values: can be any datatype and can be repeated.
''')

def inputs():
    fname = input('First Name: ')
    lname = input('Last name: ')
    degree = input('degree: ')
    major = input('Major: ')
    gpa = float(input('GPA: '))
    return fname, lname, degree, major, gpa

def diction(f, l, d, m, g):
    pydict = {}
    pydict['fname'] = f
    pydict['lname'] = l
    pydict['degree'] = d
    pydict['major'] = m
    pydict['GPA'] = g

    print('Print my_dict')
    print(pydict)
    print()
    print('Return (key:value) using built in function')
    print(pydict.items())
    print()

    print('return objects of all keys')
    print(pydict.keys())
    print()

    print('Print dictionary values')
    print(pydict.values())
    print()

    print('print only first and last name using keys')
    print(pydict['fname'], pydict['lname'])
    print()

    print('Print full name using get() function')
    print(pydict.get('fname'), pydict.get('lname'))
    print()

    print('print count of items (key:value pairs)')
    print(len(pydict))
    print()

    print('Remove last item from list')
    pydict.popitem()
    print(pydict)
    print()

    print('remove major from list using key')
    pydict.pop('major')
    print(pydict)
    print()

    print('return object type')
    print(type(pydict))
    print()

    print('clear object')
    pydict.clear()
    print(pydict)

def main():
    requirements()
    f, l, d, m, g = inputs()
    diction(f, l, d, m, g)
    

main()