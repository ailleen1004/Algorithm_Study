def solution(s):
    answer = []
    arr = list(s)
    answer.append(-1)
    for i in range(1, len(arr)):
        count = 0
        for j in range(i-1, -1, -1):
            if arr[i]==arr[j]:
                answer.append(i-j)
                count = 1
                break
        if count==0:
            answer.append(-1)
    return answer