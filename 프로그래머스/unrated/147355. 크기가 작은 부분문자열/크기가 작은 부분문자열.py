def solution(t, p):
    answer = 0
    arr = list(t)
    for i in range(len(t)-len(p)+1):
        num = 0
        for j in range(len(p)):
            num += int(arr[i+j])*pow(10, len(p)-j-1)
        if num<=int(p):
            answer += 1
    return answer