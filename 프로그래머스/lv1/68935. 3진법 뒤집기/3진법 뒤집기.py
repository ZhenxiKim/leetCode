def solution(n):
    answer = 0
    rev_base = ''
    while n>0:
        n, div = divmod(n, 3)
        rev_base += str(div)     
    answer = int(rev_base,3)
    return answer