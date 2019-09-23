#!usr/bin/env python3
import statistics as s 

def requirements():
    print('''1. Find number of students
2. Calculate percentages
3. must use float data
4. Format''')
    print()

def calculate(it, ict):
    total = it + ict
    it_tot = (it/total)
    ict_tot = (ict/total)
    return total, it_tot, ict_tot

def main():
    requirements()
    it_num = int(input('Enter number of IT students: '))
    ict_num = int(input('Enter number of ICT students: '))
    total, it_tot, ict_tot = calculate(it_num, ict_num)
    #my format method
    print(f'''Total students:\t {total:.2f}
IT Students:\t {it_tot:.2%}
ICT Students:\t {ict_tot:.2%}''')

# Other, less effect method
    '''print('{0:17} {1:>20.2f}'.format('Total Students:', total))
    print('{0:17} {1:>5.2%}'.format('IT Students:', it_tot))
    print('{0:17} {1:>5.2%}'.format('ICT Students:', ict_tot))'''
    
main()