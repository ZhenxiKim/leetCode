import re


def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r'[^\-_.a-z0-9]', '', answer)
    answer = re.sub(r'\.{2,}', '.', answer)
    # 4단계
    answer = re.sub(r"^\.", '', answer)
    answer = re.sub(r"\.$", '', answer)
    # 5 단계
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
        answer = re.sub(r"\.$", '', answer)

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer