from collections import Counter

def solution(lines):
    answer = 0
    for i in range(len(lines)):
        for j in range(1, lines[i][1]-lines[i][0]):
            lines[i].insert(j, lines[i][0]+j)
        del lines[i][len(lines[i])-1]
    com = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            com.append(lines[i][j])
    dic = Counter(com)
    arr = list(dic.values())
    for i in arr:
        if i>1:
            answer+=1
    return answer