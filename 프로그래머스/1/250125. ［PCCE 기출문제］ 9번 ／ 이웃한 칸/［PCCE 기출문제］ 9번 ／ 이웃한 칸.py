def solution(board, h, w):
    answer = 0
    
    # 상
    if h-1 >= 0:
        if board[h][w] == board[h-1][w]:
            answer += 1
    
    # 하
    if h+1 <= len(board)-1:
        if board[h][w] == board[h+1][w]:
            answer += 1
            
    # 좌
    if w-1 >= 0:
        if board[h][w] == board[h][w-1]:
            answer += 1
            
    # 우
    if w+1 <= len(board[0])-1:
        if board[h][w] == board[h][w+1]:
            answer += 1
    
    return answer