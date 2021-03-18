def network(idx, ls):
    global visit
    tg_lst = ls[idx]
    for i in range(len(ls)):
        if visit[i] == 0 and tg_lst[i] == 1:
            visit[i] = 1
            network(i, ls)
            
def solution(n, computers):
    global visit
    answer = 0
    visit = [0] * n
    for a in range(n):
        if visit[a] == 0:
            visit[a] = 1
            network(a, computers)
            answer += 1
    return answer