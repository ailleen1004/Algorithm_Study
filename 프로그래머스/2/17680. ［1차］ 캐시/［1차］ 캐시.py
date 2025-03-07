def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 5
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        
    cache = cities[:1]
    
    for c in cities[1:]:
        
        if len(cache) < cacheSize:
            
            try: # cache hit (matched)
                cache.pop(cache.index(c))
                cache.append(c)
                answer += 1

            except ValueError: # cache miss (not matched)
                answer += 5
                cache.append(c)
        
        else:
        
            try: # cache hit (matched)
                cache.pop(cache.index(c))
                cache.append(c)
                answer += 1

            except ValueError: # cache miss (not matched)
                cache.pop(0)
                answer += 5
                cache.append(c)
            
    return answer