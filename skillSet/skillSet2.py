print('''Miles Per Gallon


''')
miles = float(input('Enter miles driven: '))
gallon = float(input('Enter gallons of gas used: '))

mpg = miles/gallon
mpg = round(mpg,3)
print()
print()
print(f'{round(miles,2)} driven and {round(gallon,2)} = {round(mpg,2)} mpg')
