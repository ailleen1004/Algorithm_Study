def solution(quiz):
    answer = []
    for q in quiz:
        arr = q.split()
        if arr[1]=="+":
            result = int(arr[0]) + int(arr[2])
        elif arr[1]=="-":
            result = int(arr[0]) - int(arr[2])
        if result == int(arr[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer