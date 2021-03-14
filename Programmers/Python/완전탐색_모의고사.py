def solution(answers):
    answer = []
    supoList = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    supoCnt = [0, 0, 0]
    for i in range(len(answers)):
        ans = answers[i]
        if ans == supoList[0][i%5]:
            supoCnt[0] += 1
        if ans == supoList[1][i%8]:
            supoCnt[1] += 1
        if ans == supoList[2][i%10]:
            supoCnt[2] += 1
    supoMax = max(supoCnt)
    for i in range(3):
        if supoMax == supoCnt[i]:
            answer.append(i+1)
    return answer