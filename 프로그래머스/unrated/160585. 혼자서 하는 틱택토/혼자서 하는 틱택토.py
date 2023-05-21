def solution(board):
    answer = -1
    
    p_count=0
    o_count=0
    x_count=0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                p_count+=1
            elif board[i][j]=="X":
                x_count+=1
            else:
                o_count+=1
    
    if p_count ==9:
        answer = 1
    
    elif(((board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O")or
    (board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O")or
    (board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O")or
    (board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O")or
    (board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O")or
    (board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O")or
    (board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O")or
    (board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O"))and (x_count>=o_count)):
        answer = 0
        
    elif(((board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X")or
    (board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X")or
    (board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X")or
    (board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X")or
    (board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X")or
    (board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X")or
    (board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X")or
    (board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X"))and (o_count>=x_count+1)):
        answer = 0
    
    elif o_count<x_count:
        answer = 0
    
    elif o_count-x_count >=2:
        answer = 0
        
    else:
        answer = 1

    return answer