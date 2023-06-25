def solution(food):
    answer = ''
    for j in range(1, len(food)):
        if food[j]<2:
            continue
        for i in range(int(food[j]/2)):
            answer += str(j)
    arr = list(answer)
    answer += "0"
    for i in range(len(arr)):
        answer += arr[len(arr)-i-1]        
    return answer