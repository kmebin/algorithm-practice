import sys

n, money = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for i in range(n)]
cnt = 0

for c in list(reversed(coin)):
    if c > money:
        continue
    cnt += money // c
    money %= c

print(cnt)
