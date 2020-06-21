import sys
sys.stdin = open('b_2578.txt', 'r')

def checkBingo(t_map):
    res = 0
    cal_b = 0
    cal_c = 0
    for i in range(5):
        if sum(t_map[i]) == 0:
            res += 1
        cal_a = 0
        for j in range(5):
            cal_a += t_map[j][i]
            if i == j:
                cal_b += t_map[j][i]
            if i + j == 4:
                cal_c += t_map[j][i]
        if cal_a == 0:
            res += 1

    if cal_b == 0:
        res += 1
    if cal_c == 0:
        res += 1
    if res > 2:
        return True
    return False

def makeZero(t_map, tg_num):
    for y in range(5):
        for x in range(5):
            if t_map[y][x] == tg_num:
                t_map[y][x] = 0
                return t_map

def startGame(call_list):
    global total_map
    call_count = 0
    for y in range(5):
        for x in range(5):
            call_number = call_list[y][x]
            total_map = makeZero(total_map, call_number)
            call_count += 1
            if call_count > 10:
                if checkBingo(total_map):
                    return call_count


total_map = [list(map(int, input().split())) for _ in range(5)]
call_list = [list(map(int, input().split())) for _ in range(5)]
result = startGame(call_list)
print(result)
