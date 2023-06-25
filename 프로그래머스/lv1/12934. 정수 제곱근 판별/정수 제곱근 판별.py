def solution(n):
    answer = -1
    i = 0
    while(i*i<=n):
        i = i+1
        if i*i==n:
            answer = (i+1)*(i+1)
    return answer