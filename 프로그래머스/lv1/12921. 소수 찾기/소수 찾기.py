def solution(n):
    answer = 2
    if n==2:
        return 1
    if n==3:
        return 2
    for j in range(4, n+1):
        count = 0
        for i in range(2, int(j**(1/2))+1):
            if j%i==0:
                count = 1
                break
        if count==0:
            answer += 1
    return answer