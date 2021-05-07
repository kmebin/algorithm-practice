import sys

candy, n = map(int, sys.stdin.readline().split())
target = [int(sys.stdin.readline()) for _ in range(n)]
result = [0] * n

target.sort(reverse=True)
lack = sum(target) - candy

while lack > 0:
    lack_cnt, n_cnt = 0, 0

    if lack >= n:
        for i in range(n):
            tmp = target[i] - result[i]

            if tmp >= lack // n:
                result[i] += lack // n
                lack_cnt += lack // n
            else:
                result[i] += tmp
                lack_cnt += tmp
                n_cnt += 1

        lack -= lack_cnt
        n -= n_cnt
    else:
        for i in range(lack):
            result[i] += 1
            lack_cnt += 1

        lack -= lack_cnt

result = list(map(lambda x: x ** 2, result))
print(sum(result) % 2 ** 64)
