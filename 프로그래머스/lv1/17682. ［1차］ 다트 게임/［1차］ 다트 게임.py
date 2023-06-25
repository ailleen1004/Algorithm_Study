def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'A')
    arr = list(dartResult)
    for i in range(len(arr)):
        if arr[i]=="S":
            num = (10 if arr[i-1] == 'A' else int(arr[i-1]))
            answer.append(pow(num, 1))
        elif arr[i]=="D":
            num = (10 if arr[i-1] == 'A' else int(arr[i-1]))
            answer.append(pow(num, 2))
        elif arr[i]=="T":
            num = (10 if arr[i-1] == 'A' else int(arr[i-1]))
            answer.append(pow(num, 3))
        elif arr[i]=="*":
            answer[len(answer)-1]*=2
            if len(answer)-2>=0:
                answer[len(answer)-2]*=2
        elif arr[i]=="#":
            answer[len(answer)-1]*=(-1)
    print(answer)
    return sum(answer)