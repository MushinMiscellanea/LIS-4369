def requirements():
    print('''1. Program converts user-entered temperature into Fahrenheit or Celsius scales
2. Program comntinues to prompt user until specified not to
3. Note: upper and lowercase letters permited, though incorrect entries are not permited
4. Note: Program does not validate numeric data''' )

def convertion():
    scale = input('Fahrenheit to Celsius? Type "f", or Celsius to Fahrenheit? Type "c": ')
    scale = scale.lower()
    if scale == 'f':
        temp = float(input('Enter temperature in Fehrenheit: '))
        temp = float(((temp - 32) * 5)/9)
        print('Temperature in Celsius is:', round(temp,1))
    elif scale == 'c':
       temp = float(input('Enter temperature in Celsius: '))
       temp = float(((temp * 9)/5)+32)
       print('Temperature in Fehrenheit is:', round(temp,1))
    else: 
        print('Not a valid option')



def main():
    requirements()
    print()
    init = input('Do you want to convert a temperature (y or n)? ')
    print()
    while True:
        init = init.lower()
        if init == 'y':
            convertion()
            print()
            init = input('Do you want to convert another temperature (y or n)? ')
            print()
        elif init == 'n':
            print('Thank you for using my temperature convertion program')
            break
        else: 
            print('Incorrect entry. Please try again')
            init = input('Do you want to convert a temperature (y or n)? ')
            print()


main()