def solution(participant, completion):
    count_dict = {}
    answer = ''
    for people in participant:
        if count_dict.get(people):
            count_dict[people] += 1
        else:
            count_dict[people] = 1
    for people in completion:
        if count_dict.get(people):
            count_dict[people] -= 1
    for k, v in count_dict.items():
        if v == 1:
            answer = k
    return answer