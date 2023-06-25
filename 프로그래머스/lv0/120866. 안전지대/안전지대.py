def solution(board):
    answer = 0
    temp = [2]*len(board)
    board.insert(0, temp)
    board.insert(len(board), temp)
    for i in range(1,len(board)):
        board[i].insert(0, 2)
        board[i].insert(len(board), 2)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if board[i-1][j-1] == 0:                    
                    board[i-1][j-1] = 2
                if board[i-1][j] == 0: 
                    board[i-1][j] = 2
                if board[i-1][j+1] == 0: 
                    board[i-1][j+1] = 2
                if board[i][j-1] == 0: 
                    board[i][j-1] = 2
                if board[i][j+1] == 0: 
                    board[i][j+1] = 2
                if board[i+1][j-1] == 0: 
                    board[i+1][j-1] = 2
                if board[i+1][j] == 0: 
                    board[i+1][j] = 2
                if board[i+1][j+1] == 0: 
                    board[i+1][j+1] = 2
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                answer += 1
    return answer