def solve(lst, idx, num, tg_num):
    global answer
    if idx == len(lst):
        if num == tg_num:
            answer += 1
    else:
        solve(lst, idx+1, num + lst[idx], tg_num)
        solve(lst, idx+1, num - lst[idx], tg_num)

def solution(numbers, target):
    global answer
    answer = 0
    solve(numbers, 0, 0, target)
    return answer