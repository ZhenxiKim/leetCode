def solution(id_list, report, k):
      # 답을 담을 배열
    answer = [0 for _ in range(len(id_list))]

    # 신고 횟수 초기화
    reported = {uid: 0 for uid in id_list}

    # 신고 횟수 셋팅
    for r in set(report):  # 동일 유저에 대한 신고
        reported[r.split()[1]] += 1

    for r in set(report):  # 신고한 사람 기준으로 신고당한 사람의 정보확
        if reported[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    return answer