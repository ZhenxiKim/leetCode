def solution(participant, completion):
    answer = []
    result = {}
    for i in participant:
        result[i] = result.get(i,0) + 1
    
    for c in completion:
        result[c] -= 1
        
    for k in result:
        if result[k]:
            return k