def solution(phone_book):
    result = {}
    for i in phone_book:
        result[i] = 1

    for i in phone_book:
        for j in range(len(i)):
            if result.__contains__(i[0:j]):
                return False
    return True
