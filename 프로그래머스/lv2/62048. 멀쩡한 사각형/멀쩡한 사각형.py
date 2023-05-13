def solution(w,h):
    answer = 0
    if(w==h):
        answer = w*w-w;
    elif(w==1|h==1):
        answer =0
    else:
        for i in range(1,w):
            answer += (h*i)//w
        answer +=answer    
    return answer