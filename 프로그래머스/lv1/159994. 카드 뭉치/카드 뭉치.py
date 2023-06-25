def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1 = 0
    c2 = 0
    g = 0
    while(g<len(goal)):
        if c1<len(cards1) and goal[g]==cards1[c1]:
            c1 += 1
            g += 1
        elif c2<len(cards2) and goal[g]==cards2[c2]:
            c2 += 1
            g += 1
        else:
            answer = 'No'
            break
    return answer