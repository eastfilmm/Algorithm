def solution(name):
    a_list = {"A":0,
              "B":1,
              "C":2,
              "D":3,
              "E":4,
              "F":5,
              "G":6,
              "H":7,
              "I":8,
              "J":9,
              "K":10,
              "L":11,
              "M":12,
              "N":13,
              "O":12,
              "P":11,
              "Q":10,
              "R":9,
              "S":8,
              "T":7,
              "U":6,
              "V":5,
              "W":4,
              "X":3,
              "Y":2,
              "Z":1}
    l = len(name)
    answer = 0
    
    Min = l-1
    
    for i in range(l):
        answer+=a_list[name[i]]
        
        next = i+1
        while next<l and name[next]=="A":
            next +=1
            
        Min = min([Min,2*i+l-next,i+2*(l-next)])
    
    answer+=Min
    return answer;