import sys
sys.stdin = open('sw_2382.txt', 'r')

# 1, 2차: 22개 (런타임 에러)


def is_inbox(y, x):
    if 1 <= y < N-1 and 1 <= x < N-1:
        return True
    return False


def move():
    for k in range(K):
        d = total_map[k][3]
        total_map[k][0] += dif[d][0]
        total_map[k][1] += dif[d][1]

        # 가장자리를 밟았을 경우
        if not is_inbox(total_map[k][0], total_map[k][1]):
            total_map[k][2] = total_map[k][2] // 2
            if d in (1, 2):
                total_map[k][3] = 3 - d
            elif d in (3, 4):
                total_map[k][3] = 7 - d


def together():
    global K
    rem_lst = []
    p_dic = dict()      # 좌표: [군집의 인덱스]
    for k in range(K):
        if total_map[k][2] == 0:
            rem_lst.append(k)
            continue

        if (total_map[k][0], total_map[k][1]) not in p_dic.keys():
            p_dic.update({(total_map[k][0], total_map[k][1]): [k]})
        else:
            p_dic[(total_map[k][0], total_map[k][1])].append(k)

    new_lst = []
    for k, v in p_dic.items():
        # 두 개 이상의 군집이 만났을 경우
        if len(v) > 1:
            new_cnt = 0
            big_g = 0
            gi = -1
            for vc in v:
                if vc not in rem_lst:
                    rem_lst.append(vc)
                new_cnt += total_map[vc][2]

                if total_map[vc][2] > big_g:
                    big_g = total_map[vc][2]
                    gi = vc

            new_in = [k[0], k[1], new_cnt, total_map[gi][3]]
            new_lst.append(new_in)

    if len(rem_lst) > 0:
        rem_lst.sort(reverse=True)
        for rem in rem_lst:
            total_map.pop(rem)
            K -= 1

    if len(new_lst) > 0:
        for new in new_lst:
            total_map.append(new)
            K += 1


dif = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N, M, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(K)]     # 세로, 가로, 미생물수, 방향
    for _ in range(M):
        move()
        together()
    result = 0
    for i in range(K):
        result += total_map[i][2]
    print('#{} {}'.format(testcase, result))
