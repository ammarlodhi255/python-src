# Write a program to convert the given weight unit into another unit

weight = float(input('Enter your weight: '))
unit = input('(K)g or (L)bs: ')
KG_TO_LBS_FACTOR = 2.205

if unit.casefold() == 'k':
    weight_lbs = round(weight * KG_TO_LBS_FACTOR, 2)
    print(f'Your Weight in lbs: {weight_lbs}')
else:
    weight_kg = round(weight / KG_TO_LBS_FACTOR, 2)
    print(f'Your Weight in kg: {weight_kg}')
