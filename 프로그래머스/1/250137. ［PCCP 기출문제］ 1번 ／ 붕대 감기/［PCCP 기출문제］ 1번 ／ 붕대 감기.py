def solution(bandage, health, attacks):
    
    max_health = health
    bandage_cnt = 0
    for t in range(attacks[0][0], attacks[-1][0]+1):

        if t == attacks[0][0]:
            bandage_cnt = 0
            health -= attacks[0][1]
            if health <= 0:
                return -1
            attacks.pop(0)

        else:
            if health == max_health:
                bandage_cnt = 0

            else:
                health += bandage[1]
                bandage_cnt += 1
                if bandage_cnt == bandage[0]:
                    health += bandage[2]
                    bandage_cnt = 0
                if health > max_health:
                    health = max_health

    return health