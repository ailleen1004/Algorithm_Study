def isopening(time, op_s, op_e):
    if op_s[0]*60+op_s[1] <= time[0]*60+time[1] <= op_e[0]*60+op_e[1]:
        time = op_e.copy()
    return time

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_list = video_len.split(':')
    video_list = [int (i) for i in video_list]
    pos_list = pos.split(':')
    pos_list = [int (i) for i in pos_list]
    start_list = op_start.split(':')
    start_list = [int (i) for i in start_list]
    end_list = op_end.split(':')
    end_list = [int (i) for i in end_list]
    
    pos_list = isopening(pos_list, start_list, end_list)
    for c in commands:
        if c == 'prev':
            pos_list[1] -= 10
            if pos_list[1] < 0:
                pos_list[0] -= 1
                pos_list[1] += 60
            if pos_list[0] < 0:
                pos_list = [0, 0]
        elif c == 'next':
            pos_list[1] += 10
            if pos_list[1] >= 60:
                pos_list[0] += 1
                pos_list[1] -= 60
            if pos_list[0]*60+pos_list[1] > video_list[0]*60+video_list[1]:
                pos_list = video_list.copy()
        
        pos_list = isopening(pos_list, start_list, end_list)
    
    
    if len(str(pos_list[0])) == 1:
        pos_list[0] = '0' + str(pos_list[0])
    else:
        pos_list[0] = str(pos_list[0])
        
    if len(str(pos_list[1])) == 1:
        pos_list[1] = '0' + str(pos_list[1])
    else:
        pos_list[1] = str(pos_list[1])
        
    answer = pos_list[0] + ':' + pos_list[1]
    return answer