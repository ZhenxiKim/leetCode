def solution(players, callings):
    result = {}
    
    for idx, player  in enumerate(players):
        result[player] = idx

    for call in callings:
        past = result[call] #3
        forwardcaller = players[past -1]#kai
        result[call] -= 1
        result[forwardcaller] += 1
        players[past-1] , players[past] = players[past], players[past-1]

    return players
