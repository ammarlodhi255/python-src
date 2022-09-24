hotels = ['Crowne Plaza', 'Emerald Bay Inn',
          'Hotel Bliss', 'University Inn', 'The New View']
areas = [56.0, 20.5, 78.2, 45.8, 82.9]

for hotel, area in zip(hotels, areas):
    print(f'{hotel} with room area: {area}')