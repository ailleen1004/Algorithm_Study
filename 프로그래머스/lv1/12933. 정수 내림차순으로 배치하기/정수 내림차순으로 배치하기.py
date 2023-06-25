def solution(n):
    answer = 0
    ans = ''
    arr = list(str(n))
    arr2 = []
    for i in arr:
        arr2.append(int(i))
    arr2.sort()
    for i in range(len(arr2)):
        answer += pow(10, i)*arr2[i]
    return answer