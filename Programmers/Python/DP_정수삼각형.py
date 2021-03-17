def getMax(inList, tgList):
    res = [0] * len(tgList)
    for i in range(len(inList)):
        befNum = inList[i]
        for j in range(2):
            res[i+j] = max(res[i+j], befNum + tgList[i+j])
    return res

def solution(triangle):
    answer = 0
    for i in range(len(triangle)):
        garo = triangle[i]
        if i == 0:
            res = [garo[0]]
        else:
            res = getMax(res, garo)
    answer = max(res)
    return answer