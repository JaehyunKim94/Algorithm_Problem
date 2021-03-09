def solution(phone_book):
    answer = True
    lenList = [0] * 21
    numDict = {}
    for i in range(len(phone_book)):
        num = phone_book[i]
        len_num = len(num)
        lenList[len_num] = 1
        numDict[num] = len_num
    for k, v in numDict.items():
        if answer:
            for i in range(1, v):
                if lenList[i]:
                    check_num = k[:i]
                    if numDict.get(check_num):
                        answer = False
                        break
    return answer