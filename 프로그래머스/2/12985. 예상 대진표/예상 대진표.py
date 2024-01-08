def solution(n,a,b):
    answer = 1

    while((abs(a-b)==1 and min(a, b)%2==1) is False):
        a = int((a+1)/2)
        b = int((b+1)/2)
        answer+=1

    return answer