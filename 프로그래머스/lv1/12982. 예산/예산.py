def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget-d[i]<0:
            break
        budget -= d[i]
        answer += 1
    return answer