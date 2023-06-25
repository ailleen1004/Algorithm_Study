def solution(numlist, n):
    answer = []
    arr = []
    for i in numlist:
        arr.append([abs(n-i), i])
    arr.sort(key=lambda x: (x[0], -x[1]))
    # 0번째 인덱스 기준으로 오름차순 정렬
    #동일한 값일 경우 1번째 인덱스 기준 내림차순 졍렬
    for i in range(len(arr)):
        answer.append(arr[i][1])
    return answer