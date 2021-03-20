def solution(clothes):
    answer = 1
    cloth_dict={}
    
    for cloth in clothes:
        if cloth[-1] in cloth_dict.keys():
            cloth_dict[cloth[-1]].extend(cloth[:-1])
        else:cloth_dict[cloth[-1]]=cloth[:-1]
    #print(cloth_dict)

    for key in cloth_dict.keys():
        answer*=(len(cloth_dict[key])+1)
        #print((len(cloth_dict[key])+1))
        
    return answer-1
