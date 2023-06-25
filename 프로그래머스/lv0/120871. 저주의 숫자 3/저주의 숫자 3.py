def solution(n):
    answer = 0
    while(n>0):
        answer += 1
        if answer%3==0:
            continue
        elif answer>9:
            k = 0
            arr = list(str(answer))
            for i in arr:
                if i=="3":
                    k = 1
            if k==0:
                n -= 1
        else:
            n -= 1
    return answer