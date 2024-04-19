a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
e = float(input("Enter the value of e: "))
f = float(input("Enter the value of f: "))

print(f"\nThe system of equations is:\n{a}x + {b}y = {e}\n{c}x + {d}y = {f}")
if a * d - b * c == 0:
    print("Solution is not possible. ad-bc = 0.")

while True:
    correct = input("Is this correct? (yes or no): ")
    if correct.lower() == "yes":
        break
    elif correct.lower() == "no":
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        d = float(input("Enter the value of d: "))
        e = float(input("Enter the value of e: "))
        f = float(input("Enter the value of f: "))
        print(f"\nThe system of equations is:\n{a}x + {b}y = {e}\n{c}x + {d}y = {f}")


x = (d * e - b * f) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)

i = round(x,2)
j = round(y,2)
k = round(x)
l = round(y)

print(f"\nThe solution is:\nx = {i} or {k}\ny = {j} or {l}")
print("(" + str(i) + "," + str(j) + ") or (" + str(k) + "," + str(l) + ")")