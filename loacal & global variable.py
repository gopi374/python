# local variable
def my_function():
    local_var=10
    print(local_var)
    print()

# global variable
global_var=20
def my_function():
    print(global_var)

# modify in global variable.using global keyword without changing function name.
def my_function():
    global global_var
    gopi=40
    print(gopi)

