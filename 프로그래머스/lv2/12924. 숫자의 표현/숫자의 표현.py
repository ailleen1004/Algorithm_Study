def solution(n):
    answer = 1
    k = 1
    while(k<=(n/2)):
        sum = 0
        i = k
        while(sum<=n):
            sum+=i
            if sum==n:
                answer+=1
                break
            i+=1
        k+=1
    return answer