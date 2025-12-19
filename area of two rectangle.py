def area():
    length1 = float(input("Enter the length of the first rectangle: "))
    width1 = float(input("Enter the width of the first rectangle: "))
    length2 = float(input("Enter the length of the second rectangle: "))
    width2 = float(input("Enter the width of the second rectangle: "))
    area1 = length1 * width1
    area2 = length2 * width2
    print("Area of the first rectangle is:", area1)
    print("Area of the second rectangle is:", area2)
    if area1 > area2:
        print("The first rectangle has a greater area than the second rectangle.")
    elif area1 < area2:
        print("The first rectangle has a smaller area than the second rectangle.")
    elif area1==area2:
        print("Both rectangles have the same area.")
    else:
        print("Both rectangles have not the same area.")

# Run the program
area()
