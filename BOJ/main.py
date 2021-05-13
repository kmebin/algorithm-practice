import sys

n, k = map(int, sys.stdin.readline().split())
v = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    for j in range(v[i], k + 1):
        dp[j] += dp[j - v[i]]

print(dp[k])
