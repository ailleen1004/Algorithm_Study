def solution(new_id):
    
    # 1단계: 대문자 -> 소문자 치환
    new_id = new_id.lower()
    
    cnt_dot = 0
    answer = ''
    
    for n in new_id:
        
        # 2단계: 알파벳, 숫자, -, _를 제외한 모든 문자를 제거
        if 48<=ord(n)<=57 or 97<=ord(n)<=122 or ord(n)==45 or ord(n)==95:
            cnt_dot = 0
            answer += n
            
        # 3단계: 2번 이상 연속된 .을 하나의 .로 치환
        elif n=='.':
            cnt_dot += 1
            if cnt_dot==2:
                cnt_dot = 1
            else:
                answer += n
        
    
    # 4단계: 맨 처음 혹은 마지막으로 오는 . 삭제
    while(answer!='' and answer[0]=='.'):
        if len(answer)==1:
            answer=''
            break
        answer = answer[1:]
    
    while(answer!='' and answer[-1]=='.'):
        if len(answer)==1:
            answer=''
            break
        answer = answer[:-1]

    # 5단계: 빈 문자열이라면, a 추가
    if answer=='':
        answer='a'
    
    # 6단계: 길이가 16자 이상이면 15자까지만 남기기, 제거 후 .이 끝에 위치하면 제거
    if len(answer)>15:
        answer = answer[:15]
        while(answer[-1]=='.'):
            answer = answer[:-1]
            
    # 7단계: 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복
    if len(answer)<3:
        while(len(answer)<3):
            answer += answer[-1]
    
    return answer
    
    