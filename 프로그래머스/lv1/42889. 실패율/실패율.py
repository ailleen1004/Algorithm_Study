def solution(N, stages):
    answer = []
    arr = [0 for _ in range(N+1)]
    for i in stages:
        arr[i-1] += 1
    fail = []
    for i in range(N):
        if sum(arr[i:])!=0:
            fail.append(arr[i]/sum(arr[i:]))
        else:
            fail.append(0)
    for i in range(N):
        for j in range(N):
            if max(fail)==fail[j]:
                answer.append(j+1)
                fail[j]=-1
                break
    return answer