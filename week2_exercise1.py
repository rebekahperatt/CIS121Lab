#problem 1
'''
wide_base = float(input("What is the measure of the wide base of the trapezoid in inches? "))
narrow_base = float(input("What is the narrow base of the trapezoid in inches? "))
height = float(input("What is the height of the trapezoid in inches? "))

print(f"The area of the trapezoid is {(narrow_base + wide_base)/2 * height} in^2.")
'''
#problem 2

import math
'''
height = float(input("What is the height of the cylinder in inches? "))
radius = float(input("What is the radius of the cylinder in inches? "))

print(f"The volume of the cylinder is {math.pi * (radius**2) * height} in^2.")
'''
#problem 3
'''
radius = float(input("What is the radius of the sphere in inches? "))

print(f"The volume of the sphere is {(4/3) * math.pi * (radius**3)} in^2.")
'''
#problem 4
'''
radius = float(input("What is the radius of the semi-circle in inches? "))

print(f"The area of the semi-circle is {0.5 * math.pi * (radius**2)} in^2.")
'''
#problem 5
'''
base_edge = float(input("What is the width of the base of the pyramid in inches? "))
height = float(input("What is the height of the pyramid in inches? "))

print(f"The volume of the pyramid is {(base_edge**2) * height / 3} in^2.")
'''
#problem 6
'''
radius = float(input("What is the radius of the cone in inches? "))
height = float(input("What is the height of the cone in inches? "))

print(f"The volume of the cone is {math.pi * (((radius**2)*height)/3)} in^2.")
'''
#problem 7
'''
three_pointers = float(input("How many 3-pointers were scored? "))
two_pointers = float(input("How many 2-pointers were scored? "))

print(f"The total score for this team is {three_pointers * 3 + two_pointers * 2}.")
'''
#problem 8

chicken_count = float(input("How many chickens do you have? "))
cow_count = float(input("How many cows do you have? "))
pig_count = float(input("How many pigs do you have? "))

print(f"The total number of legs on your farm is {chicken_count * 2 + cow_count * 4 + pig_count * 4}.")
