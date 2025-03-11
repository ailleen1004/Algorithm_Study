def solution(board, moves):
    answer = 0
    basket = []
    
    for m in moves:
        
        if board[-1][m-1] == 0:
            continue
            
        for i in range(len(board)):
            if board[i][m-1] == 0:
                continue
            if len(basket) > 0:
                if board[i][m-1] == basket[-1]:
                    board[i][m-1] = 0
                    basket.pop(-1)
                    answer += 2
                    break
            basket.append(board[i][m-1])
            board[i][m-1] = 0
            break
            
    return answer

#     while(1):
#         for i in range(len(basket)):
#             # print(basket)
#             if i == len(basket)-1:
#                 return answer
            
#             if basket[i] == basket[i+1]:
#                 answer += 2
#                 basket.pop(i)
#                 basket.pop(i)
#                 break
