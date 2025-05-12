# This is a simple calculator application using Tkinter in Python.
# It allows user to find the area and perimeter of 2-dimensional shapes.

import math
# Enter which 2-dimensional shapes area and perimeter you are trying to find
shape = input("Which shapes area would you like to calculate: ").lower()
x = shape
rectangle = "rectangle"
circle = "circle"
triangle = "triangle"
hexagon = "hexagon"
trapezoid = "trapezoid"
# depending on which shape the user selects we will collect data on the 2-dimensional figure to calculate the area
# and perimeter
if x == rectangle:
# Enter dimensions of rectangle
    length = float(input("What is the length: "))
    if length >= 0:
        width = float(input("What is the width: "))
        if width >= 0:
            recPerimeter = 2 * length + 2 * width
            recArea = length * width
            rec_perimeter = round(recPerimeter, 2)
            rec_area = round(recArea, 2)
# Provide user with the area and perimeter of rectangle
            print("Shape is: rectangle")
            print("Area of rectangle is: ", rec_area)
            print("Perimeter is: ", rec_perimeter)
        else:
            print("Invalid value entered")
    else:
        print("Invalid value entered")

elif x == circle:
# Enter dimensions of circle
    radius = float(input("What is the radius: "))
    if radius >= 0:
        cirArea = (radius ** 2) * math.pi
        cirPerimeter = 2 * radius * math.pi
        cir_area = round(cirArea, 2)
        cir_perimeter = round(cirPerimeter, 2)
        print("Shape is: circle ")
# Provide user with the area and perimeter of circle
        print("Area is: ", cir_area)
        print("Perimeter is: ", cir_perimeter)
    else:
        print("Invalid value entered")

elif x == triangle:
# Enter dimensions of triangle
    base= float(input("What is length of base: "))
    if base >= 0:
        side2 = float(input("What is length of side 1: "))
        if side2 >= 0:
            side3 = float(input("What is side length of side 2: "))
            if side3 >= 0:
                height_tri = float(input("What is height of triangle: "))
                if height_tri >=0:
                    triArea = (base * height_tri) / 2
                    triPerimeter = base + side2 + side3
                    tri_area = round(triArea, 2)
                    tri_perimeter = round(triPerimeter, 2)
# Provide user with the area and perimeter of triangle
                    print("Area is: ", tri_area)
                    print("Perimeter is: ", tri_perimeter)
                else:
                    print("Invalid value entered")
            else:
                print("Invalid value entered")
        else:
            print("Invalid value entered")
    else:
        print("Invalid value entered")

elif x == hexagon:
# Enter dimensions hexagon
    sideLength = float(input("Enter side length of hexagon: "))
    if sideLength >= 0:
        hexArea = (3 * math.sqrt(3) / 2) * (sideLength ** 2)
        hexPerimeter = 6 * sideLength
        hex_area = round(hexArea, 2)
        hex_perimeter = round(hexPerimeter, 2)
# Provide user with the area and perimeter of hexagon
        print("Area of hexagon: ", hex_area)
        print("Perimeter of hexagon: ", hex_perimeter)
    else:
        print("Invalid value entered")

elif x == trapezoid:
# Input dimensions of trapezoid
    top = float(input("What is length of base: "))
    if top >= 0:
        bottom = float(input("What is height of trapezoid: "))
        if bottom >= 0:
            left_side = float(input("What is side length 1 of trapezoid: "))
            if left_side >= 0:
                right_side = float(input("What is side length 2 of trapezoid: "))
                if right_side >= 0:
                    height = float(input("What is the length of top of trapezoid: "))
                    if height >= 0:
                        trapArea = (top + bottom) / 2 * height
                        trapPerimeter = top + left_side + right_side + bottom
                        trap_area = round(trapArea, 2)
                        trap_perimeter = round(trapPerimeter, 2)
# Provide user with the area and perimeter of trapezoid
                        print("Area of trapezoid is: ", trap_area)
                        print("Perimeter of trapezoid is: ", trap_perimeter)
                    else:
                        print("Invalid value entered")
                else:
                    print("Invalid value entered")
            else:
                print("Invalid value entered")
        else:
            print("Invalid value entered")
    else:
        print("Invalid value entered")

else:
    print("Invalid value entered")