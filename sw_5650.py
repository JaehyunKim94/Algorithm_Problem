import sys
sys.stdin = open('sw_5650.txt', 'r')

# 총 50개 중
# 1, 2번시도 : 12개 - 벽에 튕길 경우 ck 바꿔주기
# 3번 시도: 13개 - 블록 마주하고 재귀 하는 방법 바꾸기
# 4번 시도: 20개 - 웜홀 방향 같게 들어오는 경우 제외
# 5번 시도: 49개 - (y좌표, x좌표, 방향)을 저장
# 6번 시도: 49개 - ck 버려도 되넹


def finish(cnt):
    cnt = cnt*2 + 1
    return cnt


def move_p(y, x, block, i):
    global cnt
    if block in range(1, 5):
        if block == 1:
            if i == 0 or i == 3:
                cnt = finish(cnt)
                return
            elif i == 1:
                cnt += 1
                i = 3
                solve(y, x, i)
            elif i == 2:
                cnt += 1
                i = 0
                solve(y, x, i)

        elif block == 2:
            if i == 1 or i == 3:
                cnt = finish(cnt)
                return
            elif i == 0:
                cnt += 1
                i = 3
                solve(y, x, i)
            elif i == 2:
                cnt += 1
                i = 1
                solve(y, x, i)

        elif block == 3:
            if i == 1 or i == 2:
                cnt = finish(cnt)
                return
            elif i == 0:
                cnt += 1
                i = 2
                solve(y, x, i)
            elif i == 3:
                cnt += 1
                i = 1
                solve(y, x, i)

        elif block == 4:
            if i == 0 or i == 2:
                cnt = finish(cnt)
                return
            elif i == 1:
                cnt += 1
                i = 2
                solve(y, x, i)
            elif i == 3:
                cnt += 1
                i = 0
                solve(y, x, i)

    elif block in range(6, 11):
        for k in range(2):
            p = block_lst[block][k]
            if p != (y, x):
                y, x = p[0], p[1]
                solve(y, x, i)
                break

    elif block == 11:
        return


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True


def solve(y, x, i):
    global cnt
    p_lst.add((y, x, i))
    yy = y + dif[i][0]
    xx = x + dif[i][1]

    if is_inbox(yy, xx):
        if (yy, xx, i) not in p_lst:
            block = total_map[yy][xx]
            if block == 0:
                solve(yy, xx, i)
            elif block == 5:
                cnt = cnt*2 + 1
                return
            else:
                move_p(yy, xx, block, i)

    else:
        cnt = finish(cnt)
        return


dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    block_lst = [[] for _ in range(12)]
    for y in range(N):
        for x in range(N):
            tg = total_map[y][x]
            if tg == -1:
                block_lst[11].append((y, x))
            else:
                block_lst[tg].append((y, x))

    result = 0
    for st in block_lst[0]:
        for i in range(4):
            cnt = 0
            p_lst = set()
            solve(st[0], st[1], i)
            if cnt > result:
                result = cnt

    print('#{} {}'.format(testcase, result))
