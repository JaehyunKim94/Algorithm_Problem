def is_wall(a):
    if 0 <= a < n:
        return True
    return False


TC = int(input())
for testcase in range(1, TC + 1):
    n = int(input())
    total_map = []
    visit = [[False for _ in range(n)] for __ in range(n)]
    cnt = 0
    cnt_lst = []

    for _ in range(n):
        new_lst = list(map(int, input().split()))
        total_map.append(new_lst)

    for y in range(n):
        for x in range(n):
            if total_map[y][x] != 0 and (not visit[y][x]):
                a, b = y, x
                cnt_y, cnt_x = 1, 1
                while True:
                    a += 1
                    if (not is_wall(a)) or total_map[a][b] == 0:
                        break
                    cnt_y += 1
                a -= 1
                while True:
                    b += 1
                    if (not is_wall(b)) or total_map[a][b] == 0:
                        break
                    cnt_x += 1
                b -= 1

                cnt_lst.append([cnt_y, cnt_x, cnt_y * cnt_x])

                for i in range(y, a + 1):
                    for j in range(x, b + 1):
                        visit[i][j] = True
                cnt += 1
    cnt_lst.sort(key=lambda element: element[2])
    kk = len(cnt_lst)
    for i in range(kk):
        for j in range(i + 1, kk):
            if cnt_lst[i][2] == cnt_lst[j][2]:
                if cnt_lst[j][0] < cnt_lst[i][0]:
                    cnt_lst[i], cnt_lst[j] = cnt_lst[j], cnt_lst[i]

    print('#{} {}'.format(testcase, cnt), end=' ')
    for lst in cnt_lst:
        for jj in range(2):
            print(lst[jj], end=' ')
    print()