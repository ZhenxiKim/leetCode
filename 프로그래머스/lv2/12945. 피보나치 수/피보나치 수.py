def solution(n):
    answer=[0] * (n)
    answer[0]= answer[1] = 1
    for i in range(2,n):
        answer[i] = answer[i-1] + answer[i-2]
    
    return answer[-1] % 1234567