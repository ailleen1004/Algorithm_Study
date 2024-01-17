def solution(elements):
    sums = []
    elements2 = elements + elements
    
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            sums.append(sum(elements2[j:j+i]))
            
    return len(set(sums))+1