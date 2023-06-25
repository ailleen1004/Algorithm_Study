def solution(keyinput, board):
    answer = [0, 0]
    for key in keyinput:
        if (-1)*int(board[0]/2)<answer[0]<=int(board[0]/2) and key=="left":
            answer[0] -= 1
        elif (-1)*int(board[0]/2)<=answer[0]<int(board[0]/2) and key == "right":
            answer[0] += 1
        elif (-1)*int(board[1]/2)<answer[1]<=int(board[1]/2) and key == "down":
            answer[1] -= 1
        elif (-1)*int(board[1]/2)<=answer[1]<int(board[1]/2) and key == "up":
            answer[1] += 1
    return answer