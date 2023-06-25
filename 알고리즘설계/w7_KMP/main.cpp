#include <iostream>
#include <chrono>
#include <vector>
#include <cmath>
#include <cstring>

using namespace std;

void kmp(char text[], char pattern[], char next[]) {
    int n = strlen(text);
    int m = strlen(pattern);

    int j = 0;
    for (int i = 0; i < n - 1; i++) {
        while (j > 0 and text[i] != pattern[j]) {
            j = next[j - 1];
        }
        if (text[i] == pattern[j]) {
            j = j + 1;
            if (j == m) {
                cout << "패턴이 발생한 위치: " << i - m + 1 << endl;
            }
        }
    }
    cout << "탐색 종료" << endl;
}

char *initNext(char *pattern) {
    int m = strlen(pattern);
    char static next[sizeof(pattern)];
    next[0] = 0;
    int j = 0;

    for (int i = 1; i < m; i++) {
        while (j > 0 and pattern[i] != pattern[j]) {
            j = next[j - 1];
        }
        if (pattern[i] == pattern[j]) {
            j += 1;
        }
        next[i] = j;
    }
    return next;
}

int main() {
    char text1[] = "ababababcababababcaabbabababcaab";
    char pattern1[] = "abababca";

    char text2[] = "This class is an algorithm design class. Therefore, students will have time to learn about algorithms and implement each algorithm themselves.";
    char pattern2[] = "algorithm";

    auto start = chrono::high_resolution_clock::now();
    //kmp(text1, pattern1, initNext(pattern1));
    kmp(text2, pattern2, initNext(pattern2));
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout << "Runtime: " << duration.count() << " seconds." << endl;

    return 0;
}
