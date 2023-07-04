def solution(s):
    if s[0]==")" or s[len(s)-1]=="(":
        return False
    left = 0
    right = 0
    for i in s:
        if i=="(":
            left+=1
        else:
            right+=1
        if left<right:
            return False
    if left!=right:
        return False
    return True