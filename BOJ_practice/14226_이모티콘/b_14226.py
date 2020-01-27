import sys
sys.stdin = open('b_14226.txt', 'r')

def BFS(obj):
    que_set = set()
    que_set.add((1, 0))
    cnt = 0
    while que_set:
        tmp_que = set()
        for num, clip in que_set:
            if num == obj:
                return cnt
            if clip > 0:
                tmp_que.add((num+clip, clip))
            if num > 2:
                tmp_que.add((num-1, clip))
            if clip != num:
                tmp_que.add((num, num))
        que_set = tmp_que
        cnt += 1

S = int(input())
result = BFS(S)
print(result)