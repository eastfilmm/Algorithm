def solution(today, terms, privacies):
    answer = []
    
    t_year, t_month, t_day = map(int,today.split("."))
     
    t_len = len(terms)
    terms_dic ={}
    for i in range(t_len):
        terms[i] = terms[i].split(" ")
        terms_dic[terms[i][0]]=int(terms[i][1])
    
    p_list = []
    p_len = len(privacies)
    for i in range(p_len):
        p_list.append(privacies[i].split(" "))
        p_year, p_month, p_day = map(int,p_list[i][0].split("."))
        month = terms_dic[p_list[i][1]]
        
        p_month += month
        while p_month > 12 : 
            p_month -= 12
            p_year +=1
        
        if p_year > t_year :
            continue
            
        elif p_year == t_year :
            if p_month > t_month :
                continue
                
            elif p_month == t_month :
                if p_day > t_day :
                    continue          
        answer.append(i+1)     

    return answer