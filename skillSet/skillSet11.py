import random as r

def requirements():
    print('''1. Get user beginning and end int value
2. Display 10 pseudo-random numbers between, and including, above values
3. Must use integer datatype
4. Example one using range() and randint()
5. Example 2 using list with range() and shuffle()''')

def random():
    floor = int(input('Enter beginning value: '))
    ceiling = int(input('Enter ending value: '))
    print()

    print('Example 1 using range() and randint()')
    for i in range(floor, ceiling+1):
        print(r.randint(floor,ceiling), end=' ')

    print()
    print()
    print('Example 2 using range() and shuffle() method')
    tsil = []
    for i in range(floor, ceiling+1):
        tsil.append(i)
    r.shuffle(tsil)
    for val in tsil:
        print(val, end=' ')
    print()
   
def main():
    requirements()
    random()

main()

