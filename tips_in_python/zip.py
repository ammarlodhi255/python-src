hotels = ['Crowne Plaza', 'Emerald Bay Inn',
          'Hotel Bliss', 'University Inn', 'The New View']
areas = [56.0, 20.5, 78.2, 45.8, 82.9]
rooms = [8, 9, 11, 25, 112]

for hotel, area, room in zip(hotels, areas, rooms):
    print(f'{hotel} with Room No. {room} has area {area} sqft.')

# If the lists are not of the same size then the zip will stop when the shortest list is exhausted
