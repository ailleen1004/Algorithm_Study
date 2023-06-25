def solution(k, m, score):
    result = 0
    score.sort(reverse=True)
    count = len(score)
    if count<m:
        return 0
    while(count>=m):
        answer = []
        for i in range(m):
            answer.append(score[len(score)-count+i])
        result += min(answer)*m
        count -= m
    return result