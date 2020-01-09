import sys
sys.stdin = open('b_2651.txt', 'r')

limit = int(input())
station = int(input())
distance = list(map(int, input().split()))
station_time = list(map(int, input().split()))

idx = -1
que = [[limit, []]]

while idx != distance:
    idx += 1
    new_que = []
    for q in que:
        dis = q[0]-distance[idx]
        lst = q[1][:]
        if dis >= 0:
            new_que.append([dis, lst])
            lst.append(idx)
            new_que.append([limit, lst])
    que = new_que[:]

print(que)