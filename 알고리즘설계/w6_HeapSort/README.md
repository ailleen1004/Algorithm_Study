# Heap Sort
## Problem
MaxHeap, MinHeap을 이용한 Heap Sort를 각 구현하시오

### 과제 1
1. 길이 10인 Random array를 생성 (0~𝑛)사이 값, 중복 무관
2. 두 가지 HeapSort를 이용하여 정렬
3. 정렬 전/후 값을 출력

### 과제 2
1. 길이 𝑛 = 2^10, 2^12, 2^14인 Random array를 생성 (0~𝑛)사이 값, 중복 무관
2. 두 가지 HeapSort를 이용하여 정렬
3. 2에 소요된 시간을 측정하여 출력 및 분석
<br/><br/>
## Result
### 과제 1
- MaxHeap
  
16 16 11 12 16 7 0 15 6 4 <br/>
0 4 6 7 11 12 15 16 16 16 <br/>
Runtime: 1.439e-06 seconds.<br/>
정렬 완료<br/><br/>

- MinHeap
  
13 0 14 19 12 18 17 5 19 4<br/>
19 19 18 17 14 13 12 5 4 0<br/>
Runtime: 3.831e-06 seconds.<br/>
정렬 완료<br/><br/>

### 과제 2
- MaxHeap
  
n=2^10 Runtime: 0.000671116 seconds.<br/>
정렬 완료
<br/><br/>
n=2^12 Runtime: 0.00297368 seconds.<br/>
정렬 완료
<br/><br/>
n=2^14 Runtime: 0.00715553 seconds.<br/>
정렬 완료
<br/><br/>

- MinHeap

n=2^10 Runtime: 0.000522394 seconds.<br/>
정렬 완료<br/><br/>

n=2^12 Runtime: 0.00187101 seconds.<br/>
정렬 완료<br/><br/>

n=2^14 Runtime: 0.00665739 seconds.<br/>
정렬 완료<br/><br/>
