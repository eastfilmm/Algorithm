def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1,rows+1):
        for column in range(1,columns+1):
            matrix[row][column] = num
            num += 1
    
    for i in queries:
        x1, y1, x2, y2 = i[0],i[1],i[2],i[3]
        Tmp = matrix[x1][y1]
        min_value = Tmp
        
        for j in range(x1,x2):
            tmp = matrix[j+1][y1]
            matrix[j][y1]=tmp
            min_value = min(tmp,min_value)
    
        for j in range(y1,y2):
            tmp = matrix[x2][j+1]
            matrix[x2][j]=tmp
            min_value = min(tmp,min_value)
            
        for j in range(x2,x1,-1):
            tmp = matrix[j-1][y2]
            matrix[j][y2]=tmp
            min_value = min(tmp,min_value)
        
        for j in range(y2,y1,-1):
            tmp = matrix[x1][j-1]
            matrix[x1][j]=tmp
            min_value = min(tmp,min_value)
        
        matrix[x1][y1+1]=Tmp
        answer.append(min_value)
    return answer