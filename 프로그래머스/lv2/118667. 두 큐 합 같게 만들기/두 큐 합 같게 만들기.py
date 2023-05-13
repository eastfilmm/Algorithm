from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    total1 = sum(queue1)
    total2 = sum(queue2)
    
    total = total1+total2
    
    if total%2!=0:
        return -1
    
    while True:
        if total1>total2:
            num = queue1.popleft()
            total1 -= num
            queue2.append(num)
            total2 += num
            answer += 1
        elif total1<total2:
            num = queue2.popleft()
            total2 -= num
            queue1.append(num)
            total1 += num
            answer +=1
        else:
            break;
        if(answer==len(queue1)*4):
            answer = -1
            break;
    return answer