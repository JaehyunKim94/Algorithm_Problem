def solution(numbers):
    answer = ''
    numList = list(map(str, numbers))
    numSort = sorted(numList, key = lambda x: x*3, reverse=True)
    answer= str(int(''.join(numSort)))         
    return answer