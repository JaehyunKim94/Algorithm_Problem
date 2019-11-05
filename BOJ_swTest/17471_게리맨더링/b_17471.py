def ck_tree(num, new_lst, lst):
    for next in con_lst[num]:
        if next in lst and next not in new_lst:
            new_lst.append(next)
            ck_tree(next, new_lst, lst)


def is_connect(lst):
    r = len(lst)
    if r == 1:
        return True
    else:
        new_lst = [lst[0]]
        ck_tree(lst[0], new_lst, lst)
        if set(new_lst) == set(lst):
            return True


def solve(k, a_lst, b_lst, a_sum, b_sum):
    global result
    if k == N:
        if a_lst and b_lst:
            res = abs(a_sum-b_sum)
            if res < result:
                if is_connect(a_lst) and is_connect(b_lst):
                    result = res

    else:
        k += 1
        a_lst.append(k)
        solve(k, a_lst, b_lst, a_sum+p_lst[k], b_sum)
        a_lst.pop()
        b_lst.append(k)
        solve(k, a_lst, b_lst, a_sum, b_sum+p_lst[k])
        b_lst.pop()


result = 999999
N = int(input())
total_map = [[0 for _ in range(N+1)] for __ in range(N+1)]
p_lst = list(map(int, input().split()))
p_lst.insert(0, 0)
con_lst = [[] for _ in range(N+1)]
for i in range(1, N+1):
    con_lst[i] = list(map(int, input().split()))[1:]
solve(0, [], [], 0, 0)
if result == 999999:
    result = -1
print(result)