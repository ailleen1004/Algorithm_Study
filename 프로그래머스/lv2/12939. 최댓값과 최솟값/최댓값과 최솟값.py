def solution(s):
    answer = ''
    a = s.split(' ')
    b = []
    for i in a:
        k = int(i)
        b.append(k)
    answer += str(min(b))
    answer += " "
    answer += str(max(b))
    return answer