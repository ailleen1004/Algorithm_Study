def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer)) #set : 중복 제거 + 오름차순 정렬
    #list까지 해줘야 배열로 저장 가능
    answer.sort() #오름차순 정렬 안해주는 경우도 있나봄
    return answer