def solution(s, n):
        answer = ''
        for c in s:
            if c != " ":
                corr = ord('A') if c.isupper() else ord('a')
                answer += chr((ord(c) - corr + n) % 26 + corr)
            else:
                answer += c
        return answer
