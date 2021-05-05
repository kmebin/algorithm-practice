import sys

n = int(sys.stdin.readline())
dice = []
for _ in range(n):
    dice.append(list(map(int, sys.stdin.readline().split())))
pair = [5, 3, 4, 1, 2, 0]  # 마주보는 쌍
maxOfSum = 0


def getMaxSide(dice, bottom, top):
    maxOfSide = 0
    for i in range(6):
        if dice[i] == bottom or dice[i] == top:
            continue
        maxOfSide = max(maxOfSide, dice[i])
    return maxOfSide


for i in range(6):
    bottom = dice[0][i]
    top = dice[0][pair[i]]
    sumOfSide = getMaxSide(dice[0], bottom, top)

    for j in range(1, n):
        for k in range(6):
            if top == dice[j][k]:
                bottom = dice[j][k]
                top = dice[j][pair[k]]
                break
        sumOfSide += getMaxSide(dice[j], bottom, top)
    maxOfSum = max(maxOfSum, sumOfSide)

print(maxOfSum)
