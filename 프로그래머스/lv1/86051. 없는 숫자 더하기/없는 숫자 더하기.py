def solution(numbers):
    answer = 0
    numbers.sort()
    arr = [10 for i in range(10)]
    for i in numbers:
        arr[i]=i
    for i in range(len(arr)):
        if arr[i]==10:
            answer += i
    return answer