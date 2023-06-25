def solution(x):
    answer = True
    arr = list(str(x))
    sum = 0
    for i in arr:
        sum += int(i)
    if x%sum!=0:
        answer = False
    return answer