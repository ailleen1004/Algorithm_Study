def solution(nums):
    answer = 0
    arr = []
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                arr.append(nums[i]+nums[j]+nums[k])
    for i in arr:
        count = 0
        for j in range(2, int(i/2)):
            if i%j==0:
                count = 1
                break
        if count==0:
            answer+=1
    return answer