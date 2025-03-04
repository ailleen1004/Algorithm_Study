from itertools import combinations 

def solution(clothes):
    answer = 1
    
    kind = []
    cnt = []
    
    clothes.sort(key=lambda x:x[1])
    
    for c in clothes:
        
        if c[1] in kind:
            cnt[-1] += 1
            
        else:
            kind.append(c[1])
            cnt.append(1)
            
    for c in cnt:
        answer *= c+1
    
    return answer-1