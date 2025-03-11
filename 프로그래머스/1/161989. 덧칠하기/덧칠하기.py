def solution(n, m, section):
    answer = 0
    
    while(section[-1] >= section[0]+m):
        
        for s in section:
            if s >= section[0]+m:
                answer += 1
                ind = section.index(s)
                section = section[ind:]
                break

    return answer+1