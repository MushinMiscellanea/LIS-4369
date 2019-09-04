print('Tip Calculator\n\n')

# collect query
cost = float(input('what is the cost of the meal? '))
heads = int(input('how many people in the party? '))

print()

# variables
tax = cost * .10
tip = cost * .10
due = cost + tax
total = cost + tax + tip
split = total/heads

#dictionaries to display data
user_in_dict = {"Cost of Meal:": cost, "tax %:": 10.0, "tip %:": 10.0, "party number:": heads}
for x, y in user_in_dict.items():
   print(f'{x} {y}')
print()
print()
print()
user_out_dict = {'Subtotal: ': cost, 'Tax: ': tax, 'Amount Due: ': due, 'Gratuity: ': tip, 'Total: ': total, 'split: ': split}
#for x, y in user_out_dict.items():
#  print(y)

 # iteration of a formatted string to include $   
for x, y in user_out_dict.items():
   print(f'{x} ${y:.2f}')