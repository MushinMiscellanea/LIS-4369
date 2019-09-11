print('''Square feet to acres

''')
sqfeet = float(input('Enter square feet: '))
acres = sqfeet/43560
acres = round(acres,3)

print(f'{sqfeet:,} sqft. = {acres:,} acres')   #this is how you format a comma
                                               # can you format comma and round in same statement????