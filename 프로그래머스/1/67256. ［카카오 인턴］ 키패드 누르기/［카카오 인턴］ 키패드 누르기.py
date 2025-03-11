def solution(numbers, hand):
    answer = ''
    keypad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    left = [0, 3]
    right = [2, 3]
    
    for n in numbers:
        if n in keypad[0]: # 왼손
            answer += 'L'
            left = [0, keypad[0].index(n)]
        elif n in keypad[2]: # 오른손
            answer += 'R'
            right = [2, keypad[2].index(n)]
        else: # 가까운 쪽 + hand
            n_index = [1, keypad[1].index(n)]
            if abs(n_index[0]-left[0]) + abs(n_index[1]-left[1]) < abs(n_index[0]-right[0]) + abs(n_index[1]-right[1]): # 왼쪽이 가까움
                answer += 'L'
                left = n_index
            elif abs(n_index[0]-left[0]) + abs(n_index[1]-left[1]) > abs(n_index[0]-right[0]) + abs(n_index[1]-right[1]): # 오른쪽이 가까움
                answer += 'R'
                right = n_index
            else: # hand
                if hand == 'left':
                    answer += 'L'
                    left = n_index
                elif hand == 'right':
                    answer += 'R'
                    right = n_index
                
    return answer