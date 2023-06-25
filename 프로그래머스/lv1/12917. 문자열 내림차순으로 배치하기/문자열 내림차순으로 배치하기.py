def solution(s):
    answer = ''
    arr = list(s)
    small = []
    big = []
    for i in arr:
        if ord(i)>=97:
            small.append(ord(i))
        else:
            big.append(ord(i))
    small.sort(reverse=True)
    big.sort(reverse=True)
    for i in small:
        answer += chr(i)
    for i in big:
        answer += chr(i)
    return answer