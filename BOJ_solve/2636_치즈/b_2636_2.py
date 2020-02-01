import sys
sys.stdin = open('2636.txt', 'r')


def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def changeAir(y, x):
    global totalMap
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if isInbox(yy, xx) and totalMap[yy][xx] == 0:
            totalMap[yy][xx] = 4
            changeAir(yy, xx)


def nearAir(y, x):
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if isInbox(yy, xx) and totalMap[yy][xx] == 4:
            return True
    return False

cheese = list()
N, M = map(int, input().split())
totalMap = [0]*N
for y in range(N):
    newInfo = list(map(int, input().split()))
    for x in range(M):
        if newInfo[x] == 1:
            cheese.append((y, x))
    totalMap[y] = newInfo
totalMap[0][0] = 4
changeAir(0, 0)
time = 0

while cheese:
    time += 1
    left_cheese = list()
    melt_cheese = list()
    for ch in cheese:
        if nearAir(ch[0], ch[1]):
            melt_cheese.append(ch)
        else:
            left_cheese.append(ch)

    if len(left_cheese) == 0:
        break

    for melt in melt_cheese:
        totalMap[melt[0]][melt[1]] = 4
        changeAir(melt[0], melt[1])
    cheese = left_cheese

print(time)
print(len(melt_cheese))