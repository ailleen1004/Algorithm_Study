# 치즈 많이 먹기
## Problem
어떤 쥐가 p[n][m] 로 구성된 미로에 있을 때, 왼쪽 아래 즉, p[n 1][0] 에서 시작하여 출구가 있는 p[0][m-1]에 도달하려고 한다.<br/>
단, 이 쥐는 항상 오른쪽 또는 위쪽으로만 움직일 수 있으며 쥐덫을 피하면서 치즈를 최대 한 많이 먹으면서 출구로 이동하여야 한다.<br/>
이 문제의 recursive property를 제시하고 먹을 수 있는 치즈의 최대값을 구하시오.

![image](https://github.com/ailleen1004/Algorithm_Study/assets/38450827/4d6914c6-8808-41d8-bed1-f92b2a8b354c)
<br/><br/>

## Result
재귀 함수: findmaxcheese()<br/>
재귀 호출 :<br/>
dp[row][col] = 1 + max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1))<br/>
dp[row][col] = max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1))<br/>

최대 치즈: 5<br/>
경로:<br/>
(8,0)->(7,0)->(6,0)->(6,1)->(5,1)->(4,1)->(4,2)->(4,3)->(3,3)->(3,4)->(2,4)->(1,4)->(1,5)->(0,5)->(0,6)->(0,7)->(0,8)
<br/><br/>
### Explanation
arr(미로)에서 치즈=1, 쥐덫=2, 나머지=0으로 표현<br/><br/>

findmaxcheese() 함수: 쥐가 먹을 수 있는 최대 치즈 개수와 그때의 경로를 dp에 저장하는 함수
- dp는 array와 같은 사이즈의 2차원 vector이고, 모두 -1로 구성되어 있다. 이는 아직 미로의 어떠한 곳도 탐색하지 않았다는 의미이며, 탐색 시 -1이 다른 값으로 바뀌어 저장된다.
- findmaxcheese의 재귀적 호출을 통하여 미로(arr)에 치즈가 있을 때, dp에 위와 오른쪽의 경우 중, 최대로 먹을 수 있는 치즈의 경우에 +1을 해주어 치즈 개수를 count해준다.
- findmaxcheese의 재귀적 호출을 통하여 미로(arr)에 치즈가 없을 때, dp에 위와 오른쪽의 경우 중, 최대로 먹을 수 있는 치즈의 경우를 그대로 갖고 와 저장한다.
- 만약 trap이 존재하면 위의 두 재귀에서 trap 경로를 선택하지 못하도록 dp에는 0을 저장한다(절대 max가 될 리 없음).<br/><br/>

main() 함수: findmaxcheese() 함수 실행 결과 즉, 최대로 먹을 수 있는 치즈 개수와 그때의 경로를 출력해주는 함수
- findmaxcheese() 함수를 실행하여 return된 결과인 dp[row][col] 즉, 출구까지 왔을 때 결론적으로 저장된 치즈 개수를 maxcheese에 할당하여 출력한다.
- 경로의 경우, dp를 바탕으로 탐색하여 입구부터 시작하여 max cheese가 저장된 경로를 따라 좌표를 출력한다.
