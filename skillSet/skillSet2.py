#!/usr/bin/env python3

def words():
    print('''Miles Per Gallon

    ''')

def calc(miles, gallon):   
    mpg = miles/gallon
    mpg = round(mpg,3)
    print('''
      ''')
    print(f'{miles:.2f} driven and {gallon:.2f} = {mpg:.2f} mpg')

def main():
    words()
    miles = float(input('Enter miles driven: '))
    gallon = float(input('Enter gallons of gas used: ')) 
    calc(miles, gallon)
    

if __name__ == "__main__":
    pass

