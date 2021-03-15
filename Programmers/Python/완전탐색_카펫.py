def getBrown(x, y):
    res = 2 * (x+y) - 4
    return res

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total):
        if total%i == 0:
            y = i
            x = total//i
            br = getBrown(x, y)
            if br == brown:
                answer.append(x)
                answer.append(y)
                break
    return answer