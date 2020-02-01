import sys
sys.stdin = open('14889.txt', 'r')


def get_point(team, num):
    pp = 0
    for t in team:
        pp += total_map[num][t]
        pp += total_map[t][num]
    return pp


def solve(k, a_team, b_team, a_point, b_point, a_num, b_num):
    global result
    if k == N-1:
        res = abs(a_point - b_point)
        result = min(res, result)
    else:
        k += 1
        if a_num < v:
            a_team.append(k)
            a_plus = get_point(a_team, k)
            solve(k, a_team, b_team, a_point+a_plus, b_point, a_num+1, b_num)
            a_team.pop()
        if b_num < v:
            b_team.append(k)
            b_plus = get_point(b_team, k)
            solve(k, a_team, b_team, a_point, b_point+b_plus, a_num, b_num+1)
            b_team.pop()


N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]
v = N // 2
result = 999999
solve(-1, [], [], 0, 0, 0, 0)
print(result)