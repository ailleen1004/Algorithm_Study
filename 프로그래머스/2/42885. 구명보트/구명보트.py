def solution(people, limit):
    answer = 0
    left = 0
    right = len(people)-1
    
    people.sort()
    
    while(left<right):
        if people[left]+people[right]<=limit:
            left = left+1
            answer = answer+1
        right = right-1
        
    return len(people)-answer