import collections
def solution(genres, plays):
    answer = []
    dict={}
    sum_list=[]
    
    #딕셔너리로 정리
    for i in range(len(genres)):
        if genres[i] in dict.keys():
            dict[genres[i]].insert(-1,plays[i])
            dict[genres[i]][-1].append(i)
        else:dict[genres[i]]=[plays[i],[i]]
    print(dict)
    
    # sum_list 구축
    for key in dict.keys():
        tmp=dict[key]
        sum_list.append(sum(dict[key][:-1]))
    print(sum_list.index(max(sum_list)))
    print(sum_list)
    
    for _ in range(len(sum_list)):
        print(dict.keys())
        genre=list(dict.keys())[sum_list.index(max(sum_list))]
        print(genre)
        if len(dict[genre])==2:
            answer.append(dict[genre][-1][0])
        else:
            answer.append(dict[genre][-1][ dict[genre][:-1].index(max(dict[genre][:-1])) ])
            dict[genre][dict[genre][:-1].index(max(dict[genre][:-1]))]=0
            answer.append(dict[genre][-1][ dict[genre][:-1].index(max(dict[genre][:-1])) ])
            
        sum_list[sum_list.index(max(sum_list))]=0
        print(sum_list)
        print(answer)
    
    
    return answer
