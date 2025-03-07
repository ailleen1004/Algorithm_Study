def solution(s):
    answer = []
    
    l = []
    ll = []
    lll = []
    tmp = 0
    k = 0
    
    ss = s[1:-1]
    
    for i in range(len(ss)):
        
        if k==1:
            k=0
            continue
        
        if i == len(ss)-1: # 마지막 튜플일 때
            cnt = len(l)-1
            for j in l:
                tmp += j*pow(10, cnt)
                cnt -= 1
                
            ll.append(tmp)
            lll.append(ll)
            continue
            
        if ss[i]=="{": # 튜플 시작
            continue
        
        if ss[i]=="}" and ss[i+1]==",": # 튜플 끝

            cnt = len(l)-1
            for j in l:
                tmp += j*pow(10, cnt)
                cnt -= 1
                
            ll.append(tmp)
            lll.append(ll)
            ll = []
            l = []
            k = 1
            tmp = 0
            continue
        
        if ss[i]==",":
            
            cnt = len(l)-1
            for j in l:
                tmp += j*pow(10, cnt)
                cnt -= 1
            ll.append(tmp)
            l = []
            tmp = 0
            continue
        
        l.append(int(ss[i]))
    
    lll.sort(key=len)
    
    for i in lll:
        for j in i:
            if j not in answer:
                answer.append(j)
                    
    return answer