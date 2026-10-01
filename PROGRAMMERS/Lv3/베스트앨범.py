def solution(genres, plays):
    playlist = {}
    answers = []
    for i in range(len(genres)):
        if genres[i] not in playlist:
            playlist[genres[i]] = [(plays[i], i)]
        else:
            playlist[genres[i]].append((plays[i], i))
            playlist[genres[i]].sort(key=lambda x: (-x[0], x[1]))
            
    new_pl = sorted(playlist, key=lambda g: sum(p for p, _ in playlist[g]), reverse=True)

    for g in new_pl:
        for p, idx in playlist[g][:2]:
            answers.append(idx)
    return answers