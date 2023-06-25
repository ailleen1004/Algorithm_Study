def solution(s):
    answer = 1
    count = [0, 0]
    start = s[0]
    i=0
    while(i<len(s)):
        if start==s[i]:
            count[0]+=1
        elif start!=s[i]:
            count[1]+=1
        if count[0]==count[1] and i<len(s)-1:
            answer+=1
            start=s[i+1]
            count[0]=0
            count[1]=0
        i+=1
    return answer