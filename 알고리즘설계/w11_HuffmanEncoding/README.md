# Huffman Encoding
## Problem
주어진 string 을 Huffman code table 을 구하고, 이를 이용해서 압축하는 프로그램을 작성하시오
<br/><br/>
## Result
Huffman code table:<br/>
 :00<br/> 
a:11000<br/>
e:11001<br/>
g:1001<br/>
h:11010<br/>
i:101<br/>
n:1000<br/>
r:11011<br/>
s:111<br/>
t:01<br/>
Input string: this is a test string<br/>
Encoded string: 01110101011110010111100110000001110011110100111011101110110001001
<br/><br/>
## Explanation
강의노트를 참고하여 buildHuffmanTree 함수를 통해 Huffman code table을 출력하고, generateHuffmanCodes 함수를 통해 위 Table을 바탕으로 “this is a test string”을 encoding한 결과를 출력하였다.<br/>
먼저 알파벳의 빈도수를 for문을 통해 계산하여 symbol과 frequency에 각각 데이터, 빈도수를 저장하고 PQ에 push하였습니다. 그 다음 for문을 통해 Huffman Tree를 만들고, Huffman table과 table을 바탕으로 encoding한 결과를 모두 출력하였다.

