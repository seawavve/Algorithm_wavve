import collections

def solution(participant, completion):
    answer = ''
    p=collections.Counter(participant)
    c=collections.Counter(completion)
    #print(p)
    #print(c)
    
    result=p-c
    #print(list(result.keys())[0])
    return list(result.keys())[0]
