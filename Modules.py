import sys
sys.path.append("D:\\Code-files\\Visual code\\Python modules")
from my_module import test_str

point_1 = [0, 0]
point_2 = [0, 0]

point_1[0], point_1[1] = input("Enter two points of the first coordinate: ").split(', ')
point_1[0] = int(point_1[0])
point_1[1] = int(point_1[1])

point_2[0], point_2[1] = input("Enter two points of the second coordinate: ").split(', ')
point_2[0] = int(point_2[0])
point_2[1] = int(point_2[1])

dist = "%.3f" % calc_dist(point_1, point_2)

print(f"Distance between ({point_1[0]}, {point_1[1]}) and ({point_2[0]}, {point_2[1]}) is: {dist}")
