def solution(message, spoiler_ranges):
    important = []
    
    # 단어는 공백으로 구분, 소문자 + 문자
    # 문자 하나라도 스포 방지 -> 스포 방지 단어로 간주
    # 다른 곳에서 사용한 적 없고, 이전 스포 방지 단어와 중복되지 않으면 중요한 단어로 판단
    # 이 때 왼쪽부터 순서대로 판단
    
    # solution
    # 0. 모자이크 처리??
    # 1. 모자이크 걸치는 구간의 단어를 순서대로 찾아야 함
    # 2. 그 단어가 다른 문장에 모자이크 되지 않은 단어와 겹치는지 확인해야함
    # 3. 이전에 모자이크로 중요한 단어로 선정되었는지 확인
    # 4. 중요한 단어로 리스트에 등록
    # 5. 리스트 길이를 출력
    
    words = message.split()
    copy = ""
    spo_range = []
    for spo in spoiler_ranges:
        for idx in range(spo[0], spo[1] + 1):
            spo_range.append(idx)
            
    for i in range(len(message)):
        if i in spo_range:
            if message[i] == ' ':
                copy += ' '
            else:
                copy += '*'
        else:
            copy += message[i]
    
    copy_words = copy.split()
    candidates = []
    words_length = len(words)
    
    for j in range(words_length):
        if words[j] != copy_words[j]:
            candidates.append(words[j])
            words[j] = 'A'
    
    for cd in candidates:
        if cd in words or cd in important:
            continue
        important.append(cd)
    
    return len(important)