def solution(n):
    answer = 0
    word = str(n)
    arr = list(word)
    for i in arr:
        answer += int(i)
    return answer