import random
lot = [[0,random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2)],[0,0,0,0,0,0,0],[0,random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2)],[0,random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2)],[0,0,0,0,0,0,0],[0,random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2)]]
free = 0

for a in lot:
  print(a)
for b in range(len(lot)):
  for c in range(len(lot[0])):
    if lot[b][c] == 1:
      free += 1

print(free)
