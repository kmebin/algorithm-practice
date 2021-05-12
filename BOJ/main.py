import sys

n = int(sys.stdin.readline())

d = [0] * (n + 1)

for i in range(n + 1):
    if i == 0 or i == 1 or i == 2:
        d[i] = i
    else:
        d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[n])
