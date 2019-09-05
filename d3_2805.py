import sys
sys.stdin = open('2805.txt', 'r')


def solve():
    middle = N//2
    res = sum(total_map[middle])
    pm = -1
    for y in range(0, middle):
        pm += 1
        res += sum(total_map[y][middle-pm:middle+pm+1])

    for y in range(middle+1, N):
        res += sum(total_map[y][middle-pm:middle+pm+1])
        pm -= 1
    return res


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = []
    for _ in range(N):
        st_in = input()
        new_lst = []
        for j in range(N):
            new_lst.append(int(st_in[j]))
        total_map.append(new_lst)
    result = solve()
    print('#{} {}'.format(testcase, result))

