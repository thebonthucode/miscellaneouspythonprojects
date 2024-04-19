print("put numbers below")
a = input()
b = input()

print("symbol:(+,-,x,/)")
symbol = input()

if symbol == '+':
  print(a + b)
elif symbol == "-":
  print([int(a) - int(b)])
elif symbol == "x":
  print([int(a) * int(b)])
elif symbol == "/":
  print([int(a) / int(b)])
  