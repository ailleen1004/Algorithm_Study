def solution(n, m):
    answer = [0, 0]
    for i in range(1, max(n, m)+1):
        if n%i==0 and m%i==0:
            answer[0] = i
    j=max(n, m)
    while(j%n!=0 or j%m!=0):
        j+=1
    answer[1] = j
    return answer