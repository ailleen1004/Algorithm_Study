def solution(s, skip, index):
    answer = ''
    alpha = []
    for i in range(26):
        if chr(i+97) in skip:
            continue
        else:
            alpha += chr(i+97)
    for i in s:
        find = alpha.index(i)
        answer += alpha[(find + index) % (len(alpha))]
    return answer