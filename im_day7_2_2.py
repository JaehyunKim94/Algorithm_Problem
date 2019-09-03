import sys
sys.stdin = open('im_day7_2.txt', 'r')


TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    ck = 0
    node_lst = []
    visit = [False for _ in range(N*M)]
    for _ in range(M):
        pk = ck
        new_lst = list(map(int, input().split()))
        com_num = new_lst[0]
        for i in range(N):
            node_lst.append([ck+i-1, new_lst[i], ck+i+1])

        for i in range(ck):
            if node_lst[i][1] > com_num:
                pk = i  # 삽입할 위치 찾기

                node_lst[node_lst[pk][0]][2] = ck   # pk의 pre node 의 next node는 새로운 노드의 시작점으로 바뀌고
                node_lst[ck][0] = node_lst[pk][0]   # 새로운 리스트의 pre node 는 pk의 pre node와 같다

                node_lst[ck+N-1][2] = pk            # 새로운 리스트의 next node 는 pk
                node_lst[pk][0] = ck + N - 1         # pk의 pre node는 새로운 노드의 마지막 지점이고
                break
        ck += N
        print(node_lst)


    for i in range(N*M):
        if node_lst[i][0] == -1:
            s_p = i
            break

    for i in range(N*M):
        print(node_lst[s_p][1], end=' ')
        s_p = node_lst[s_p][2]

    print()