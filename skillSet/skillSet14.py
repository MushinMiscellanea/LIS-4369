import re, operator

def req():
    print('''1. Program calculates two numbers and rounds to 2 decimal places
2. Promt user for two numbers and a suitable operator
3. Use error handling to validate data
4. test for correct operator
5. division by zero no permited
6.program loops until correct input is gather''')

    
def num_validation(num):
    try:
        num = float(num)
        return num
    except ValueError:
        print('not a valid option')
        return

def op_val():
    while True:
        operator = input('Enter Operator: ' )
        j = re.match('[-|+|/|*|%|//|**]', operator)
        if j:
            return operator
        else: 
            print('Invalid operator')
            continue


def calculate(num1, num2, oper):
    while True:
        ## dictionary matching oper to builtin operator function
        ops = { 
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '//': operator.floordiv,
            '%': operator.mod,
            '**': operator.pow}
        ## set matched dict key to value (operator function)
        op_func = ops[oper]
        try:
            a = op_func(num1,num2)
            return a
        except ZeroDivisionError:
            print('Cannot divide by zero')
            num2 = input('Enter num2: ')
            num2 = num_validation(num2)
            oper = op_val()
            continue



def main():
    req()
    # this while loop is for the end prompt to make anouther calculation
    while True:
        # this while loop is for num1 validation
        while True:
            num1 = input('Enter num1: ')
            num1 = num_validation(num1)
            if isinstance(num1, float):
                break
            else: continue 
        # the while loop is for num2 validation
        while True:
            num2 = input('Enter num2: ')
            num2 = num_validation(num2)
            if isinstance(num2, float):
                break
            else: continue
        # operator
        op = op_val()
        # calculation
        answer = calculate(num1, num2, op)
        print(f'{answer:,.f}')
        ## prompt to make another calculation
        again = input('Would you like to make another calculation ("y" or "n"): ')
        again = again.lower()
        if again == 'n':
            print('Thank you for calculating')
            break
        else: continue

    


main()