def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        targetList = array[i-1:j]
        print(targetList)
        sortedTarget = sorted(targetList)
        answer.append(sortedTarget[k-1])
    return answer