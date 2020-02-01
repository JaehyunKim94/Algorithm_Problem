import sys
sys.stdin = open('b_2643.txt', 'r')


def is_good(downPaper, upPaper):
    if downPaper[0] >= upPaper[0] and downPaper[1] >= upPaper[1]:
        return True
    return False


N = int(input())
paperList = [(0, 0)]*N
for k in range(N):
    a, b = map(int, input().split())
    paperList[k] = (max(a, b), min(a, b))
paperList.sort()
countList = [1]*N
idx = 0
while idx < N-1:
    idx += 1
    for i in range(idx):
        if is_good(paperList[idx], paperList[i]):
            countList[idx] = max(countList[idx], countList[i]+1)
print(max(countList))
