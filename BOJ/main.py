import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for item in data:
    k = 1
    for _item in data:
        if _item[0] > item[0] and _item[1] > item[1]:
            k += 1
    print(k, end=' ')