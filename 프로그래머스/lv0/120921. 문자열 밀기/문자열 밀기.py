def solution(A, B):
    answer = 0
    arrA = list(A)
    arrB = list(B)
    if A == B:
        return answer
    for i in range(len(arrA)):
        answer = 0
        arrB.append(arrB[i])
        for j in range(len(arrA)):
            if arrA[j] != arrB[i+j+1]:
                answer = -1
                break
        if answer != -1:
            answer = i+1
            break
    return answer