def solution(progresses, speeds):
    answer = []
    
    days = [0 for _ in range(len(progresses))]
    
    for i in range(len(progresses)):
        
        while(progresses[i] < 100):
            
            progresses[i] += speeds[i]
            days[i] += 1
    
    ans = 1
    max_day = days[0]
    
    for d in range(1, len(days)):
        
        if max_day < days[d]:
            answer.append(ans)
            ans = 1
            max_day = days[d]
        
        else:
            ans += 1
    
    answer.append(ans)
    
    return answer