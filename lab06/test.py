x = "<<global x>>"
y = "<<global y>>"

def g(x: str):
    """x will be bound by a call, and y by assignment, 
    so both x and y will be local variables.
    """
    y = x 
    print(f"The value of x is '{x}' while g is executing")
    print(f"The value of y is '{y}' while g is executing")

print(f"x is {x}, y is {y} before calling g(y)")
print("========  Calling g ========")
g(y)
print("========  After call to g ====")
print(f"x is '{x}', y is '{y}' after calling g(y)")    