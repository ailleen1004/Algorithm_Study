def solution(n, left, right):
    answer = []
    row = list(range(1, n+1))
    
    
    for i in range(int(left/n)-1, int(right/n)):
        if i == n-1:
            break
        for j in range(0, i+1):
            row[j] += i-j+1
        answer.append(row)
        row = list(range(1, n+1))
        
    # print(answer)
    answer = sum(answer,[])
            
    return answer[left%n:len(answer)-(n-right%n)+1]