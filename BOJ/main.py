import sys

n = int(sys.stdin.readline())
fibo = [0] * (n + 1)

for x in range(n + 1):
    if x == 0 or x == 1:
        fibo[x] = x
    else:
        fibo[x] = fibo[x - 1] + fibo[x - 2]

print(fibo[n])
