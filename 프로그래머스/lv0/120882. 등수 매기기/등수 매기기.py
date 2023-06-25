def solution(score):
    answer = [1 for i in range(len(score))]
    avg = []
    for i in range(len(score)):
        avg.append((score[i][0]+score[i][1])/2)
    for i in range(len(avg)):
        for j in range(len(avg)):
            if avg[i]<avg[j]:
                answer[i] += 1
    return answer