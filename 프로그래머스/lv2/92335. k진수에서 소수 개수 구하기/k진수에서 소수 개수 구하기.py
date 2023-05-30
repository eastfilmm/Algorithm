def solution(n, k):
    answer = 0
    
    num = ""
    
    while n>0:
        tmp = n%k
        num= str(tmp)+num
        n=n//k
    
    list = num.split("0")
    isTrue = 0

    for i in list:
        if len(i)==0:
            continue
        if int(i)<2:
            continue
        for j in range(2,int(int(i)**0.5)+1):
            if int(i)%j==0:
                isTrue = 1
                break;
        if isTrue !=1:
            answer+=1
            
    return answer