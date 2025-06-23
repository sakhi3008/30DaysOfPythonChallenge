# Challenge 2 --  Calculate the area of a rectangle using user-input length and width

# way 1 - Basic input & print
length = float(input('Enter the length of a rectangle: '))
width = float(input('Enter the width of a rectangle: '))
area = length * width 
print('Calculated area:',area)

# way 2 - Using Function
def calculate_area(length, width):
    return length * width

length = float(input('Enter the length of a rectangle: '))
width = float(input('Enter the width of a rectangle: '))
area = calculate_area(length , width)
print(f"Calculated area: {area}") 

#way 3 - Using Lambda function
calculate_area = lambda l, w: l*w
length = float(input('Enter the length of a rectangle: '))
width = float(input('Enter the width of a rectangle: '))
print(calculate_area(length , width))

# way 4 - Using map() & split() for input
length, width = map(float, input("Enter length and width separated by space: ").split())
print('Calculated area:',length * width)

# way 5 - Using a Dictionary
rectangle = {}
rectangle['length'] = float(input('Enter the length of a rectangle: '))
rectangle['width'] = float(input('Enter the width of a rectangle: '))
area = rectangle['length'] * rectangle['width']
print(area)

# way 6 - Using a class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input('Enter the length of a rectangle: '))
width = float(input('Enter the width of a rectangle: '))
rect = Rectangle(length, width)
print(rect.area())

# way 7 - With Error Handling
def calculate_area(length, width):
    return length * width

try:
    length = float(input("Enter the length of a rectangle: "))
    width = float(input("Enter the width of a rectangle: "))
    print("Area of the rectangle is:", calculate_area(length, width))
except ValueError:
    print("Please enter valid integer values for length and width.")

