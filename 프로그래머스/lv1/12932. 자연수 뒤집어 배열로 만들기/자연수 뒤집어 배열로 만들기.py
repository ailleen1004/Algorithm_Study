def solution(n):
    answer = []
    arr = list(str(n))
    for i in range(len(arr), 0, -1):
        answer.append(int(arr[i-1]))
    return answer