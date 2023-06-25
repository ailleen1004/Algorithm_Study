def solution(k, score):
    answer = [score[0]]
    last = [score[0]]
    for i in range(1, len(score)):
        count = 0
        for j in range(len(answer)):
            if score[i]>answer[j]:
                answer.insert(j, score[i])
                count = 1
                break
        if count==0:
            answer.append(score[i])
        if i<k:
            last.append(answer[len(answer)-1])
        else:
            last.append(answer[k-1])
    return last