def solution(s):
    answer = ''
    arr = list(s)
    if len(arr)%2==1:
        answer = answer + arr[int(len(arr)/2)]
    else:
        answer = answer + arr[int(len(arr)/2)-1]
        answer = answer + arr[int(len(arr)/2)]
    return answer