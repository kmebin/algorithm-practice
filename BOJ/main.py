import sys

# 식량창고 개수
n = int(sys.stdin.readline())
# 각 식량창고에 저장된 식량의 개수
k = list(map(int, sys.stdin.readline().split()))
k.insert(0, 0)

d = [0] * (n + 1)
d[1] = k[1]

for i in range(2, n + 1):
    d[i] = max(d[i - 2] + k[i], d[i - 1])

print(d[n])
