def solution(nums):
    answer = 0
    arr = list(set(nums))
    if len(arr)<=(len(nums)/2):
        answer = len(arr)
    else:
        answer = len(nums)/2
    return answer