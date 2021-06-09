from collections import deque

def solution(n, edge):
    answer = 0
    totalMap = [[] for _ in range(n+1)]
    for x, y in edge:
        totalMap[x].append(y)
        totalMap[y].append(x)
        
    q = deque()
    q.append(1)
    route = [0] * (n+1)
    route[1] = 1
    
    while q:
        now = q.popleft()
        for m in totalMap[now]:
            if route[m] == 0:
                q.append(m)
                route[m] = route[now] + 1
    maxRoute = max(route)
    answer = route.count(maxRoute)
    return answer