import math
def requirements():
    print('''1. Program calculates sphere volume in liquid US gallonsfrom user entered diameter value in inches, and rounds to two decimal places
2. Must use pythons builtin pi() and pow() methods.
3. programs checks from none integer types
4. Program continues to prompt for user entry until specified not to.''')

def calc():
    diameter = input('Please enter diameter in inches: ')
    print()
    # exception handeling for input data type
    try:
        diameter = int(diameter)
    except ValueError:
        print()
        print("invalid data type")
        return
    r = diameter/2
    v = round((4/3*math.pi*pow(r,3))/231,2)
    print(f'Sphere volume: {v} liquid US gallons')
    


def main():
    requirements()
    print()
    initial_in = input('Do you want to calculate the volume of a sphere ("y" or "n")? ')
    initial_in = initial_in.lower()
    print()
    while True:             #program iterator
        if initial_in == 'y':
            calc()
            print()
            initial_in = input('would you like to make another calculation("y" or "n")? ')
            print()
        elif initial_in == 'n':
            print()
            print('Thank you for using the sphere volume calculator')
            break
        else:
            initial_in = input('Invalid option...Do you want to calculate the volume of a sphere ("y" or "n")? ')
            print()

main()