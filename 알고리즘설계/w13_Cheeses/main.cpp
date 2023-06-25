#include <iostream>
#include <vector>

using namespace std;

#define n 9 // arr row
#define m 9 // arr col

vector<vector<int>> arr = { // ma
        {0, 0, 1, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 1, 0, 2, 0},
        {1, 0, 2, 0, 0, 0, 0, 1, 0},
        {0, 0, 0, 0, 1, 2, 0, 0, 0},
        {0, 1, 0, 1, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 2, 1, 2, 0},
        {0, 1, 0, 0, 1, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 1, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0}
};
// 1: cheese, 2: trap, 0: nothing
vector<vector<int>> dp(n, vector<int>(m, -1)); // 9*9 -1 array
// -1: not yet visited

int findmaxcheese(int row, int col) {
    if (row < 0 || col < 0 || row >= n || col >= m) { // out of range
        return 0;
    }

    if (dp[row][col] != -1) { // already visited
        return dp[row][col];
    }

    if (arr[row][col] == 1) { // cheese
        dp[row][col] = 1 + max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1)); // max cheese + 1
    }
    else if (arr[row][col] == 2) { // trap
        dp[row][col] = 0;
    }
    else { // nothing
        dp[row][col] = max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1)); // max cheese

    }

    return dp[row][col];
}

int main() {
    int maxcheese = findmaxcheese(n - 1, 0);

    cout << "재귀 함수: findmaxcheese()" << endl;
    cout << "재귀 호출 : " << endl;
    cout << "dp[row][col] = 1 + max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1))" << endl;
    cout << "dp[row][col] = max(findmaxcheese(row - 1, col), findmaxcheese(row, col + 1))" << endl << endl;

    cout << "최대 치즈: " << maxcheese << endl;
    cout << "경로: " << endl;

    int row = n - 1;
    int col = 0;

    while (row != 0 || col != m - 1) { // until get to the exit
        cout << "(" << row << "," << col << ")->";
        if (row > 0  && col < m - 1 && dp[row - 1][col] >= dp[row][col + 1]) { // up >= right
            row = row - 1;

        }
        else if (row > 0 && col < m - 1 && dp[row - 1][col] < dp[row][col + 1]) { // up < right
            col = col + 1;

        }
        else if (row == 0) { // cannot go up
            col = col + 1;
        }
        else if (col == m - 1) { // cannot go right
            row = row - 1;
        }
    }
    cout << "(0," << m - 1 << ")" << endl; // exit

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
