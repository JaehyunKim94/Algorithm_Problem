import sys
sys.stdin = open('14890.txt', 'r')


def is_flat(lst, idx, visit, udck):
    if udck == 1:       # 내리막길 이라면
        for kk in range(idx+1, idx+X+1):
            if lst[idx+1] != lst[kk] or visit[kk] == 1:
                return False
    elif udck == 2:     # 오르막길 이라면
        for kk in range(idx, idx-X, -1):
            if lst[idx] != lst[kk] or visit[kk] == 1:
                return False
    return True


def is_good(lst):
    global cnt
    visit = [0 for _ in range(N)]     # 공사 여부 체크
    for p in range(N-1):
        updown = abs(lst[p] - lst[p+1])
        if updown == 1:     # 높이 차가 1일 때, 낮은 지형이 평평한지 체크
            if p < X-1 and lst[p] < lst[p + 1]:
                return
            elif p > N - X - 1 and lst[p] > lst[p + 1]:
                return

            else:
                if lst[p] > lst[p+1]:   # 내리막길
                    if is_flat(lst, p, visit, 1):
                        for jj in range(p+1, p+X+1):
                            visit[jj] = 1
                    else:
                        return

                else:       # 오르막길
                    if is_flat(lst, p, visit, 2):
                        for jj in range(p, p-X, -1):
                            visit[jj] = 1
                    else:
                        return

        elif updown > 1:    # 높이 차가 2 이상인 경우
            return
    cnt += 1


N, X = map(int, input().split())
ck_lst = [0 for _ in range(2*N)]
for i in range(N):
    ck_lst[i] = list(map(int, input().split()))
for y in range(N):
    new_lst = []
    for x in range(N):
        new_lst.append(ck_lst[x][y])
    ck_lst[N+y] = new_lst

cnt = 0
for i in range(2*N):
    is_good(ck_lst[i])
print(cnt)