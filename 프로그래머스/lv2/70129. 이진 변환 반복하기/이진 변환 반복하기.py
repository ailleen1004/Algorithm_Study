def solution(s):
    answer = [0, 0]
    while s!="1":
        answer[1]+=s.count("0")
        x = s.replace("0", "")
        if x=="1":
            answer[0]+=1
            break
        num = len(x)
        l = []
        while num>1:
            rem = num%2
            num = int(num/2)
            l.append(str(rem))
        l.append(str(num))
        l.reverse()
        s = ''
        s = ''.join(l)
        answer[0]+=1
    return answer