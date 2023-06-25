# 치즈 많이 먹기
## Problem
어떤 쥐가 p[n][m] 로 구성된 미로에 있을 때, 왼쪽 아래 즉, p[n 1][0] 에서 시작하여 출구가 있는 p[0][m-1]에 도달하려고 한다.<br/>
단, 이 쥐는 항상 오른쪽 또는 위쪽으로만 움직일 수 있으며 쥐덫을 피하면서 치즈를 최대 한 많이 먹으면서 출구로 이동하여야 한다.<br/>
이 문제의 recursive property를 제시하고 먹을 수 있는 치즈의 최대값을 구하시오.

![image](https://github.com/ailleen1004/Algorithm_Study/assets/38450827/4d6914c6-8808-41d8-bed1-f92b2a8b354c)


## Result
재귀 함수: findmaxcheese()<br/>
재귀 호출 :<br/>
dp[row][col] = 1 + max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1))<br/>
dp[row][col] = max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1))<br/>

최대 치즈: 5<br/>
경로:<br/>
(8,0)->(7,0)->(6,0)->(6,1)->(5,1)->(4,1)->(4,2)->(4,3)->(3,3)->(3,4)->(2,4)->(1,4)->(1,5)->(0,5)->(0,6)->(0,7)->(0,8)
