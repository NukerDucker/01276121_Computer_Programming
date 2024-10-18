def rectangle_area(length, width):
    return length * width

def main():
    print("Rectangle Area Calculator")
    width, length = input("Enter the width & length : ").split()
    width, length = int(width), int(length)
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()