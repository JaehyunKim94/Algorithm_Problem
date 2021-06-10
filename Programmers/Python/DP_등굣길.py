def solution(m, n, puddles):
    answer = 0
    totalMap = [[0] * (m+1) for _ in range(n+1)]
    for x, y in puddles:
        totalMap[y][x] = -1
    for x in range(1, m+1):
        if totalMap[1][x] == -1:
            break
        totalMap[1][x] = 1
    for y in range(1, n+1):
        if totalMap[y][1] == -1:
            break
        totalMap[y][1] = 1
    
    print(totalMap)
    for y in range(1, n+1):
        for x in range(1, m+1):
            if totalMap[y][x] == 0:
                if totalMap[y][x-1] > 0:
                    totalMap[y][x] += totalMap[y][x-1]
                if totalMap[y-1][x] > 0:
                    totalMap[y][x] += totalMap[y-1][x]
    answer = totalMap[n][m] % 1000000007
    
    return answer