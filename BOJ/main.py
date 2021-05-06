import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n = int(sys.stdin.readline())
    applicant = []
    cnt = 1

    for _ in range(n):
        applicant.append(list(map(int, sys.stdin.readline().split())))

    applicant.sort()
    target = applicant[0][1]

    for i in range(1, n):
        if target > applicant[i][1]:
            cnt += 1
            target = applicant[i][1]

    print(cnt)
