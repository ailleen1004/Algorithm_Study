def solution(wallet, bill):
    answer = 0
    
    while(1):
        
        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[0] >= bill[1] and wallet[1] >= bill[0]):
                return answer
        
        ind = bill.index(max(bill))
        bill[ind] = int(bill[ind]/2)
        answer += 1
        
    
    return answer