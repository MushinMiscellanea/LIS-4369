def req():
    print('''1. prompt user for two numbers
2. use python selection structure
3. est for correct operator
4. display''')

def calc(a, b, c):
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '/':
        print(a/b)
    elif c == '*':
        print(a*b)
    elif c == '//':
        print(a//b)
    elif c == '%':
        print(a%b)
    elif c == '**':
        print(pow(a,b))
    else:
        print('wrong input')

def main():
    req()
    num1 = int(input('Num1: '))
    num2 = int(input('Num2: '))
    op = input('Operator: ')
    calc(num1, num2, op)

main()
