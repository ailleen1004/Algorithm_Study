def solution(sizes):
    answer = 0
    max1 = []
    max2 = []
    for i in sizes:
        max1.append(max(i))
        max2.append(min(i))
    answer = max(max1)*max(max2)        
    return answer