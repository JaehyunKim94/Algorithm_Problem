import sys
sys.stdin = open('1974.txt', 'r')

def ch_gs():
    global result
    for y in range(9):
        a_que = []
        b_que = []
        for x in range(9):
            if total_map[y][x] not in a_que:
                a_que.append(total_map[y][x])
            else:
                result = 0
                return
            if total_map[x][y] not in b_que:
                b_que.append(total_map[x][y])
            else:
                result = 0
                return

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            c_que = []
            for i in range(3):
                for j in range(3):
                    if total_map[y+i][x+j] not in c_que:
                        c_que.append(total_map[y+i][x+j])
                    else:
                        result = 0
                        return

TC = int(input())
for testcase in range(1, TC+1):
    total_map = []
    for _ in range(9):
        new_lst = list(map(int, input().split()))
        total_map.append(new_lst)
    result = 1
    ch_gs()
    print('#{} {}'.format(testcase, result))