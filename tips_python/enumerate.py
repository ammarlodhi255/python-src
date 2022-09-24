areas = [56.0, 20.5, 78.2, 45.8, 82.9]

for index, area in enumerate(areas):
    print(f'Room {index + 1}: {area} sq. ft.')


# Example where enumerate is useful:
# The following lists correspond with each other and we want to traverse through each of these lists
hotels = ['Crowne Plaza', 'Emerald Bay Inn',
          'Hotel Bliss', 'University Inn', 'The New View']
areas = [56.0, 20.5, 78.2, 45.8, 82.9]

for index, hotel in enumerate(hotels):
    print(f'Hotel: {hotel}, Room area: {areas[index]}')
