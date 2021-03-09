def solution(genres, plays):
    answer = []
    play_dict = {}      
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if play_dict.get(genre):
            play_dict[genre][0] += play
            play_dict[genre][1].append((play, i))
        else:
            play_dict[genre] = [play, [(play, i)]]
    dict_sort = sorted(play_dict.items(), key= lambda x: x[1], reverse=True)
    for item in dict_sort:
        sorted_v = sorted(item[1][1], key = lambda x: (x[0], -x[1]), reverse=True)[:2]
        for play, idx in sorted_v:
            answer.append(idx)
    return answer