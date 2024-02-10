# Define a function to calculate the area of a rectangle
def rectangle(width, height):
    # Calculate the area (width multiplied by height)
    area = width * height
    # Print the area with a descriptive message
    print(f"The area of the rectangle is {area} square units.")


# Call the rectangle function with width=4 and height=5
rectangle(4, 5)

# Define another function to calculate the area of a rectangle
# Improved naming for clarity


def calculate_rectangle_area(width, height):
    # Calculate the area and store it in a variable
    area = width * height
    # Use an f-string for more readable code
    print(f"The area of the rectangle is {area} square units.")


# Call the calculate_rectangle_area function with named arguments for clarity
calculate_rectangle_area(width=4, height=5)
