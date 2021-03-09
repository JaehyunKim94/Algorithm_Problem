def solution(clothes):
    answer = 0
    cloth_dict = {}
    res = 1
    for cloth in clothes:
        name, part = cloth
        if cloth_dict.get(part):
            cloth_dict[part] += 1
        else:
            cloth_dict[part] = 2
    for k, v in cloth_dict.items():
        res *= v
    answer = res-1
    return answer