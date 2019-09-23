def requirements():
    print('''1. find calories of fat, arbs, and protein.
2. Calculate percentages
3. Must use float datatypes
4. Format, Right-allign number, and round to two decimal places''')
    print()

def calculate(fat, carbs, protein):
    fat_cal = fat * 9
    carb_cal = carbs * 4
    protein_cal = protein * 4
    return fat_cal, carb_cal, protein_cal

def main():
    tot_fat = float(input('Input total fat grams: '))
    tot_carbs = float(input('Input total carb grams: '))
    tot_prot = float(input('Input total protein grams: '))
    f, c, p = calculate(tot_fat, tot_carbs, tot_prot)
    total = f + c + p
    fat_perc = f / total
    carb_perc = c / total
    prot_perc = p / total
    print('{0}{1:>15}{2:>15}'.format('Type', 'Calories', 'Percentage'))
    print('{0}{1:>15.2f}{2:>15.2%}'.format('Fat', f, fat_perc))
    print('{0}{1:>13.2f}{2:>15.2%}'.format('Carbs', c, carb_perc))
    print('{0}{1:>11.2f}{2:>15.2%}'.format('Protein', p, prot_perc))
main()