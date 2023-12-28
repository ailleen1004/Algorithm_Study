def solution(s):
    comp = []
    
    for i in s:
        if len(comp)==0:
            comp.append(i)
        elif comp[-1]==i:
            comp.pop()   
        else:
            comp.append(i)
    
    if len(comp)==0:
        return 1
    else:
        return 0