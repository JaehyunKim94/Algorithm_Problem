def solution(numbers):
    global answerSet
    answer = 0
    answerSet = set()
    visit = [0] * len(numbers)
    getNumbers('', visit, numbers)
    answer = len(answerSet)
    print(answerSet)
    return answer

def getNumbers(res, visit, numbers):
    global answerSet
    if len(res) > 0:
        checkNum = int(res)
        if checkNum > 1 and isPrime(checkNum):
            answerSet.add(checkNum)
            
    for i in range(len(numbers)):
        if(visit[i] == 0):
            visit[i] = 1
            getNumbers(res+numbers[i], visit, numbers)
            visit[i] = 0
        
def isPrime(num):
    if num ==2 or num == 3:
        return True
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    return True