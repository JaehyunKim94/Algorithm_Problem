import sys
sys.stdin = open('d3_5201.txt', 'r')

TC = int(input())
for testcse in range(1, TC+1):
    N, M = map(int, input().split())
    n_lst = sorted(list(map(int, input().split())))     # 화물
    m_lst = sorted(list(map(int, input().split())))     # 트럭
    n_lst.reverse()
    m_lst.reverse()
    visit = [0 for _ in range(N)]
    result = 0
    for m in m_lst:
        for i in range(N):
            if n_lst[i] <= m:
                if not visit[i]:
                    visit[i] = 1
                    result += n_lst[i]
                    break
    print('#{} {}'.format(testcse, result))