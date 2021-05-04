import sys
import itertools

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0

for r in range(1, n + 1):
    nCr = list(itertools.combinations(data, r))
    for item in nCr:
        if s == sum(item):
            cnt += 1

print(cnt)
