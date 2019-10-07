def solve(k):
    global cnt
    if k == N-1:
        cnt += 1
    else:
        k += 1
        for i in range(4):
            lst_b.append(i)
            solve(k)
            lst_b.pop()

def num_com(k):
    global cnt_a
    if k == N-1:
        cnt_a += 1
        print(lst_c)
    else:
        k += 1
        for i in range(1, 14):
            if visit[i] == 0:
                visit[i] = 1
                lst_c.add(i)
                num_com(k)
                lst_c.pop()
                visit[i] = 0


N = 5
lst_a = [[i+1 for i in range(13)]]
for i in range(3):
    lst_a.append([i+1 for i in range(13)])

total_lst = []
cnt = 0
cnt_a = 0
lst_b = []
solve(-1)
lst_c = set()
visit = [0 for _ in range(14)]
num_com(-1)
print(cnt, cnt_a)