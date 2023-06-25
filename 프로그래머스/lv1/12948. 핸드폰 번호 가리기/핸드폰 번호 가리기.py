def solution(phone_number):
    answer = ''
    arr = list(phone_number)
    for i in range(len(arr)-4):
        arr[i] = "*"
    for i in arr:
        answer = answer + i
    return answer