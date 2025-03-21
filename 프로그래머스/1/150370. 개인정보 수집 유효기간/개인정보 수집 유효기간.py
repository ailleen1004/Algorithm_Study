def solution(today, terms, privacies):
    answer = []
    
    index = 1
    today = today.split('.')
    today_num = []
    for t in today:
        today_num.append(int(t))
    
    new_terms = {}
    for t in terms:
        t = t.split(' ')
        new_terms[t[0]] = int(t[1])

    for p in privacies:
        p = p.split(' ')
        p_date = p[0].split('.')
        p_date_num = []
        for d in p_date:
            p_date_num.append(int(d))
        
        # 날짜 더하기
        p_date_num[0] += int(new_terms[p[1]]/12)
        p_date_num[1] += int(new_terms[p[1]]%12)
        if p_date_num[1] > 12:
            p_date_num[0] += 1
            p_date_num[1] -= 12
        
        if p_date_num[0] < today_num[0]:
            answer.append(index)
            
        elif p_date_num[0] == today_num[0]:
            if p_date_num[1] < today_num[1]:
                answer.append(index)
                
            elif p_date_num[1] == today_num[1]:
                if p_date_num[2] <= today_num[2]:
                    answer.append(index)
            
        index += 1
    
    return answer