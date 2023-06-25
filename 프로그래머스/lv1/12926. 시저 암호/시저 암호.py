def solution(s, n):
    answer = ''
    arr = list(s)
    for i in arr:
        if i==" ":
            answer += " "
        elif (90<ord(i)+n and 65<=ord(i)<=90) or 122<ord(i)+n:
            answer += chr(ord(i)+n-26)
        else:
            answer += chr(ord(i)+n)
    return answer