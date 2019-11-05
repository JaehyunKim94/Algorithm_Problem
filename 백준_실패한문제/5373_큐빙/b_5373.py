import sys
sys.stdin = open('b_5373.txt', 'r')


def rotate_up(tg, pom):
    global cube
    tg_face = cube[tg]
    line_idx = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
    rotate_line = [tg_face[line_idx[i][0]][line_idx[i][1]] for i in range(8)]
    if pom == '+':
        for i in range(8):
            line = line_idx[i]
            y, x = line[0], line[1]
            idx = i + 2
            if idx > 7:
                idx -= 8
            cube[tg][y][x] = rotate_line[idx]
    else:
        for i in range(8):
            line = line_idx[i]
            y, x = line[0], line[1]
            idx = i + 6
            if idx > 7:
                idx -= 8
            cube[tg][y][x] = rotate_line[idx]


def rotate(tg, pom):
    global cube
    rotate_up(tg, pom)
    if tg in (0, 1):
        pass
    elif tg in (2, 3):
        pass
    elif tg in (4, 5):
        pass


# 위 아래 앞 뒤 왼 오른
dir_book = {'U': 0, 'D': 1, 'F': 2, 'B':3, 'L': 4, 'R': 5}
color = ['w', 'y', 'r', 'o', 'g', 'b']
TC = int(input())
for testcase in range(TC):
    cube = [[[color[i]] * 3 for _ in range(3)] for i in range(6)]
    n = int(input())
    change_lst = list(input().split())
    for change in change_lst:
        rotate(dir_book[change[0]], change[1])