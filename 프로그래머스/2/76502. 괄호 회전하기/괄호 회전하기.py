def solution(s):
    answer = 0
    brackets = s * 2
    
    for i in range(len(s)):
        b = brackets[i:i+len(s)]
        temp = ""
        
        while(b!=temp):
            temp = b[:]
            b = b.replace('[]', '')
            b = b.replace('{}', '')
            b = b.replace('()', '')
            
            if len(b)==0:
                answer+=1
                break
                
    return answer