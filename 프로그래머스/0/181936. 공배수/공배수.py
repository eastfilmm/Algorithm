def solution(number, n, m):
    answer = 0
    a = number%n
    b = number%m
    
    if a==0 and b==0 :
        answer = 1
    else:answer = 0
    return answer