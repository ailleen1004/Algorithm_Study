def solution(s):
    answer = ''
    arr = s.split(" ")
    for i in arr:
        for j in range(len(i)):
            if j%2==0:
                answer += i[j].upper()
            elif j%2==1:
                answer += i[j].lower()
        answer += " "
    return answer[0:-1]