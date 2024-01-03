def solution(k, tangerine):
    answer = 0
    count = [0 for _ in range(max(tangerine))]
    
    for t in tangerine:
        count[t-1] = count[t-1]+1
    
    count.sort(reverse=True)
    
    while(k>0):
        k = k-count[answer]
        answer = answer+1
    
    return answer