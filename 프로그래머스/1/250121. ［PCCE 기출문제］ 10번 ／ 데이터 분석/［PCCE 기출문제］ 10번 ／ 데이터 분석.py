def solution(data, ext, val_ext, sort_by):
    answer = []
    
    exts = ['code', 'date', 'maximum', 'remain']
    ext_ind = exts.index(ext)
    sort_ind = exts.index(sort_by)
    
    for d in data:
        if d[ext_ind] < val_ext:
            answer.append(d)
            
    answer.sort(key=lambda x:x[sort_ind])
    
    return answer