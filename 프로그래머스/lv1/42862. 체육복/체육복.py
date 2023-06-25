def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort()
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            answer+=1
        elif lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer+=1
        elif lost[i]+1 in reserve and lost[i]+1 not in lost:
            reserve.remove(lost[i]+1)
            answer+=1
    return answer