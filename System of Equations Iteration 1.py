a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
e = float(input("Enter the value of e: "))
f = float(input("Enter the value of f: "))

print("You entered the following system of equations:\n{a}x + {b}y = {e}\n{c}x + {d}y = {f}")
correct_input = input("Is this correct? (y/n): ")

while correct_input.lower() != 'y':
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))
    e = float(input("Enter the value of e: "))
    f = float(input("Enter the value of f: "))
    print("You entered the following system of equations:\n{a}x + {b}y = {e}\n{c}x + {d}y = {f}")
    correct_input = input("Is this correct? (y/n): ")

if a*d - b*c == 0:
    print("Error: ad - bc = 0. Solution is not possible.")
else:
    x = (d*e - b*f) / (a*d - b*c)
    y = (a*f - c*e) / (a*d - b*c)
    print("x = " + str({x}))
    print("y = " + str({y}))
