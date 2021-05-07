import sys

candy, n = map(int, sys.stdin.readline().split())
target = [int(sys.stdin.readline()) for _ in range(n)]
result = 0

target.sort()
lack = sum(target) - candy

for i in range(n):
    cnt = min(target[i], lack // (n - i))
    lack -= cnt
    result += cnt ** 2

print(result % 2 ** 64)
