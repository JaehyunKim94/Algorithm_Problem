def solution(citations):
    answer = 0
    totalBook = len(citations)
    sortedCitations = sorted(citations)
    cntDict = {}
    for c in sortedCitations:
        if cntDict.get(c):
            cntDict[c] += 1
        else:
            cntDict[c] = 1
    for i in range(totalBook+1):
        if totalBook >= i:
            answer = i
        else:
            break
        
        if cntDict.get(i):
            totalBook -= cntDict[i]
        else:
            continue
    return answer