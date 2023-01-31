import math 

print("Ammars module")

test_str = "This is a test string from 'my_module'"

def calculate_distance(point_1, point_2):
    x1 = point_1[0]
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]

    dist = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
    return dist




