# 1. Insertion Sort
## Problem
Insertion Sort를 구현하는 함수 insertionSort

아래 기능을 가진 main 함수

1. 길이 𝑛인 Random array를 생성 (0~𝑛)사이 값 , 중복 무관
2. insertionSort를 이용하여 정렬
3. 2에 소요된 시간을 측정하여 출력
4. 소요시간 2초 이상인 𝑛 사용
<br/><br/>
## Result
Runtime: 0.676853 seconds.

정렬 완료
<br/><br/>

# 2. Shell Sort
## Problem
Shell Sort를 구현하는 함수 shellSort1, shellSort2, shellSort3

아래의 서로 다른 Gap sequence를 이용하는 세 가지 함수를 작성

- [N/(2^𝑘)] : [N/2], [N/4], ... , [N/(2^𝑘)], ... , 1
- 𝑘 = 3∗𝑘+1 : ... , 121, 40, 13, 4, 1
- 𝑘 = 11∗𝑘+1 : ... , 1464, 133, 12, 1
- NOTE : gap은 큰 수 -> 작은 수 순서로 적용함, 항상 n보다 작음, 마지막은 1

아래 기능을 가진 main 함수

1. 길이 𝑛인 Random array 를 생성 (0~𝑛) 사이 값, 중복 무관
2. shellSort를 이용하여 정렬
3. 2에 소요된 시간을 측정하여 출력
4. 𝑘 = 3∗𝑘+1 sequence 기준 2초 이상인 𝑛 사용
<br/><br/>
## Result
### [N/(2^𝑘)]
Runtime: 11.7834 seconds.

정렬 완료

### 𝑘 = 3∗𝑘+1
Runtime: 5.59317 seconds.

정렬 완료

### 𝑘 = 11∗𝑘+1
Runtime: 8.11141 seconds.\
정렬 완료
