def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0]
    for i in range(len(answers)):
        if stu1[i%len(stu1)]==answers[i]:
            ans[0]+=1
        if stu2[i%len(stu2)]==answers[i]:
            ans[1]+=1
        if stu3[i%len(stu3)]==answers[i]:
            ans[2]+=1
    answer.append(1)
    for i in range(1, 3):
        if ans[answer[0]-1]<ans[i]:
            del answer[0]
            answer.append(i+1)
        elif ans[answer[0]-1]==ans[i]:
            answer.append(i+1)
    return answer