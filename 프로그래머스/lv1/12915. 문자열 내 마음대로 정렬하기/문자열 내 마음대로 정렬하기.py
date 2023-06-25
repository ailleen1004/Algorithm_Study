def solution(strings, n):
    answer = []
    result = []
    strings.sort()
    for i in range(len(strings)):
        arr = list(strings[i])
        answer.append([arr[n], i])
    print(answer)
    answer.sort()
    for i in range(len(answer)):
        result.append(strings[answer[i][1]])
    return result