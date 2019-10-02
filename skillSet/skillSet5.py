import random as r

def req():
    print('''1. Get user bigenning and ending values
2. display random values between that range
3. Must use intenger datatypes
4. Example 1: use range() and randint() functions.
5. Example 2: Use a list with range() and randint() functions.''')
    print()


def list(f, c):
    for i in range(10):
        l.append(r.randint(f,c))
    print()
    
l = []   


def main():
    req()
    print('Input')
    floor = int(input('Enter floor value: '))
    ceiling = int(input('Enter ceiling value: '))

    list(floor, ceiling)
    
    print('output')
    s = (f'{l[0]}, {l[1]}, {l[2]}, {l[3]}, {l[4]}, {l[5]}, {l[6]}, {l[7]}, {l[8]}, {l[9]}')
    print(s)


    
    

main()

    


    