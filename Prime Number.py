import time                      
timeinit = time.time()

is_prime = [True] * 1000

is_prime[0] = is_prime[1] = False

for i in range(2, int(1000 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1000, i):
            is_prime[j] = False

for i in range(1000):
    if is_prime[i]:
        print(i)

timefinal = time.time()
elapsedtime = timefinal-timeinit
print("Elapsed Time:" + str(elapsedtime))