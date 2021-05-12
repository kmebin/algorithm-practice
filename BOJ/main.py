import sys

n = int(sys.stdin.readline())
w = [int(sys.stdin.readline()) for _ in range(n)]
w.insert(0, 0)

d = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        d[i] = w[i]
    elif i == 2:
        d[i] = w[i] + w[i - 1]
    else:
        d[i] = max(d[i - 1], max(w[i] + d[i - 2], w[i] + w[i - 1] + d[i - 3]))

print(d[n])
