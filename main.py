print("Please enter the dimensions of the room in sqft")

def calculate_area(w, h):
    area_sqft = w * h
    print(f"The total square foot is: {area_sqft}")

width = int(input("Enter the width of the room: "))
height = int(input("Enter the height of the room: "))

calculate_area(width, height)
