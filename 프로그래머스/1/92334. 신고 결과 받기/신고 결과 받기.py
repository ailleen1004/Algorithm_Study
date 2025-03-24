def solution(id_list, report, k):
    answer = []
    
    id_singonum_dic = {}
    id_singoid_dic = {}
    
    for i in id_list:
        id_singonum_dic[i] = 0
        id_singoid_dic[i] = []
    
    set_report = list(set(report))
    for r in set_report:
        r_split = r.split(' ')
        id_singonum_dic[r_split[1]] += 1
        id_singoid_dic[r_split[0]].append(r_split[1])
    
    for key, val in id_singoid_dic.items():
        ans = 0
        for singo in val:
            if id_singonum_dic[singo] >= k:
                ans += 1
        answer.append(ans)
    
    return answer