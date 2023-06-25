#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int knapsack(int bag, const vector<pair<int, int>>& jewl) {
    int s = jewl.size();
    vector<vector<int>> dp(s + 1, vector<int>(bag + 1, 0));

    for (int i = 1; i <= s; i++) {
        int weight = jewl[i - 1].first;
        int value = jewl[i - 1].second;
        for (int j = 1; j <= bag; j++) {
            if (weight <= j) {
                dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j]);
            }
            else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return dp[s][bag];
}

int main() {
    int bag1 = 15;
    vector<pair<int, int>> jewl1 = { make_pair(5, 5), make_pair(10, 7), make_pair(7, 10), make_pair(3, 6), make_pair(4, 8), make_pair(11, 20) };

    int max_value1 = knapsack(bag1, jewl1);
    cout << "Maximum value that can be obtained: " << max_value1 << endl;

    int bag2 = 30;
    vector<pair<int, int>> jewl2 = { make_pair(3, 5), make_pair(7, 7), make_pair(8, 10), make_pair(5, 6), make_pair(6, 8), make_pair(13, 20), make_pair(11, 18), make_pair(2, 5) };

    int max_value2 = knapsack(bag2, jewl2);
    cout << "Maximum value that can be obtained: " << max_value2 << endl;

    return 0;
}
