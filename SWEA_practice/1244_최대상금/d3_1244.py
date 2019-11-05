import sys
sys.stdin = open('d3_1244.txt', 'r')


def lsttonum(num_lst):
    res = 0
    for i in range(ran):
        res += num_lst[i] * (10 ** (ran-i-1))
    return res


def solve():
    ma_num = -1
    ma_in = -1

    for i in range(ran-1, -1, -1):
        if num_lst[i] > ma_num:
            if num_lst[i] != max_lst[i]:
                ma_num = num_lst[i]
                ma_in = i

    if ma_in == -1:
        if ck:
            num_lst[ran-2], num_lst[ran-1] = num_lst[ran-1], num_lst[ran-2]

    else:
        tg_in = -1
        for i in range(ran):
            if num_lst[i] < ma_num:
                tg_in = i
                break
        if tg_in != -1:
            visit[0].append(tg_in)
            visit[1].append(ma_in)
            num_lst[tg_in], num_lst[ma_in] = num_lst[ma_in], num_lst[tg_in]


TC = int(input())
for testcase in range(1, TC+1):
    N, M = input().split()  # N: 초기 숫자    M: 반복 횟수
    M = int(M)
    # 자릿수 계산
    ran = len(N)

    # N 을 리스트 형태로 변환
    num_lst = [0 for _ in range(ran)]
    for i in range(ran):
        num_lst[i] = int(N[i])

    ck = True
    ck_set = set(num_lst)
    if len(num_lst) != len(ck_set):
        ck = False

    visit = [[], []]
    max_lst = sorted(num_lst, reverse=True)
    for _ in range(M):
        solve()
    v_len = len(visit[0])

    if v_len > 1:
        for i in range(v_len-1):
            for j in range(i+1, v_len):
                if num_lst[visit[0][i]] == num_lst[visit[0][j]]:
                    if num_lst[visit[1][j]] < num_lst[visit[1][i]]:
                        num_lst[visit[1][j]], num_lst[visit[1][i]] = num_lst[visit[1][i]], num_lst[visit[1][j]]

    print('#{} {}'.format(testcase, lsttonum(num_lst)))