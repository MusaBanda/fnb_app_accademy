import math

side = float(input("Enter the length of a side: "))

# Square
square_area = side ** 2
square_perimeter = 4 * side

# Equilateral Triangle
triangle_area = (math.sqrt(3) / 4) * side ** 2
triangle_perimeter = 3 * side

# Cube
cube_surface_area = 6 * (side ** 2)
cube_volume = side ** 3

print("\n--- Results ---")
print(f"Square -> Area: {square_area}, Perimeter: {square_perimeter}")
print(f"Equilateral Triangle -> Area: {triangle_area:.2f}, Perimeter: {triangle_perimeter}")
print(f"Cube -> Surface Area: {cube_surface_area}, Volume: {cube_volume}")
