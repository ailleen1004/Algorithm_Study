def solution(citations):
    
    citations.sort(reverse=True)
    
    if citations[-1]>len(citations):
        
        return len(citations)
        
    for c in range(len(citations)):
        
        if citations[c] <= len(citations[:c+1]):
            
            return max(citations[c], len(citations[:c+1])-1)
        