from collections import deque

def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    x,y = 0,0
    for i in range(row):
        for j in range(col):
            if(board[i][j]=='R'):
                x,y = i,j
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs():
        queue = deque()
        queue.append((x,y))
        visited = [[0]*col for _ in range(row)]
        visited[x][y]=1
        
        while queue:
            popx, popy = queue.popleft()
            if(board[popx][popy]=='G'):
                return visited[popx][popy]
            for i in range(4):
                nx,ny = popx,popy
                while True:
                    nx, ny = nx+dx[i],ny+dy[i]
                    if nx<0 or nx>=row or ny<0 or ny>=col:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if 0<=nx<row and 0<=ny<col and board[nx][ny]=='D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny]= visited[popx][popy] + 1
                    queue.append((nx,ny))
        return -1
    
    answer = bfs()
    if answer >0:
        answer -= 1
    return answer