def solution(players, callings):
    answer = []
    
    players_dic_pg = {}
    players_dic_gp = {}
    
    for i, p in enumerate(players):
        players_dic_pg[p] = i
        players_dic_gp[i] = p
    # 	{'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    #   {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}
        
    for c in callings:
        c_grade = players_dic_pg[c]
        past_player = players_dic_gp[c_grade-1]
        players_dic_pg[c] -= 1
        players_dic_pg[past_player] += 1
        players_dic_gp[c_grade] = past_player
        players_dic_gp[c_grade-1] = c
    
    players_dic = dict(sorted(players_dic_pg.items(), key=lambda item: item[1]))
    answer = list(players_dic.keys())
    return answer