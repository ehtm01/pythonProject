def solution(video_len, pos, op_start, op_end, commands):
    # 10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다.
    # 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다.
    # pos = 0 if pos < 10 else pos - 10
    # 영상의 처음 위치는 0분 0초입니다.
    
    # 10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 
    # 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
    
    # 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
    
    vm, vs = map(int, video_len.split(':'))
    vls = vm * 60 + vs
    
    pm, ps = map(int, pos.split(':'))
    pls = pm * 60 + ps
    
    osm, oss = map(int, op_start.split(':'))
    osls = osm * 60 + oss
    
    oem, oes = map(int, op_end.split(':'))
    oels = oem * 60 + oes
    
    for command in commands:
        if osls <= pls <= oels:
            pls = oels
            
        if command == 'prev':
            pls = 0 if pls < 10 else pls - 10
            
        else:
            pls = vls if pls > vls - 10 else pls + 10
            
    if osls <= pls <= oels:
        pls = oels

    h, m = divmod(pls, 60)
    h = '0' + str(h) if h // 10 < 1 else str(h)
    m = '0' + str(m) if m // 10 < 1 else str(m)
    return h + ':' + m
