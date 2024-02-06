def triangle_area(base,height):
    return 0.5 * base * height

base = float(input("Enter base of the triangle:"))
height = float(input("Enter height of the triangle: "))
area = triangle_area(base,height)

print(f"The area of a triangle with base {base} and height {height} is: {area}")

