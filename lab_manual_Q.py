'''# Method 1: Using lists for student data
def display_students_with_lists():
 print("=== Method 1: Using Lists ===")

 # Student data in separate lists
names = ["Alice Johnson", "Bob Smith", "Carol Davis",
"David Wilson", "Emily Brown"]
ages = [20, 19, 21, 22, 20]
print("S.no\tName\t\t\tAge")
print("-"*40)
for i in range(len(names)):
    print(f"{i+1}.\t{names[i]:<20}\t{ages[i]}")


file=open("new.txt", "w") 
file.write("Hello, this is a single line.\n")
file.write("This is another line.\n")
lines=["lin1\nline2\nline3\nline4"]
file.writelines(lines)
print(file)
file.close()



def pyramid_pattern(rows):
    print("\nPyramid Pattern:")
    for i in range(1, rows + 1):
 # Print spaces
        spaces = " " * (rows - i)
 # Print stars
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    for i in range(rows-1,0,-1):
 # Print spaces
        spaces = " " * (rows - i)
 # Print stars
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    for i in range(rows):
        print("*"*i)
pyramid_pattern(5)
'''

