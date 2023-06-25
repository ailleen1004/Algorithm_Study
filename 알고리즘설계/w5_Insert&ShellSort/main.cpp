#include <iostream>
#include <chrono>
#include <vector>

#define len 10000000

using namespace std;

vector<int> randomVector(int n) {
    vector<int> vec(n);
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        vec[i] = rand() % 100; // Generating random integers between 0 to 99
    }
    return vec;
}

void ShellSort1(vector<int>& arr) {
    int i, j, tmp;
    int gap = len / 2;
    while (gap > 0) {
        for (i = gap; i < len; i++) {
            tmp = arr[i];
            j = i;
            while (j >= gap and arr[j - gap] > tmp) {
                arr[j] = arr[j - gap];
                j = j - gap;
            }
            arr[j] = tmp;
        }
        gap = gap / 2;
    }
    for (i = 1; i < len; i++) { //gap=1
        tmp = arr[i];
        j = i;
        while (j >= 1 and arr[j - 1] > tmp) {
            arr[j] = arr[j - 1];
            j = j - 1;
        }
        arr[j] = tmp;
    }
}

void ShellSort2(vector<int>& arr) {
    int i, j, tmp;
    int gap = (len - 1) / 3;
    while (gap > 0) {
        for (i = gap; i < len; i++) {
            tmp = arr[i];
            j = i;
            while (j >= gap and arr[j - gap] > tmp) {
                arr[j] = arr[j - gap];
                j = j - gap;
            }
            arr[j] = tmp;
        }
        gap = (gap - 1) / 3;
    }
    for (i = 1; i < len; i++) { //gap=1
        tmp = arr[i];
        j = i;
        while (j >= 1 and arr[j - 1] > tmp) {
            arr[j] = arr[j - 1];
            j = j - 1;
        }
        arr[j] = tmp;
    }
}

void ShellSort3(vector<int>& arr) {
    int i, j, tmp;
    int gap = (len - 1) / 11;
    while (gap > 0) {
        for (i = gap; i < len; i++) {
            tmp = arr[i];
            j = i;
            while (j >= gap and arr[j - gap] > tmp) {
                arr[j] = arr[j - gap];
                j = j - gap;
            }
            arr[j] = tmp;
        }
        gap = (gap - 1) / 11;
    }
    for (i = 1; i < len; i++) { //gap=1
        tmp = arr[i];
        j = i;
        while (j >= 1 and arr[j - 1] > tmp) {
            arr[j] = arr[j - 1];
            j = j - 1;
        }
        arr[j] = tmp;
    }
}

void InsertionSort(vector<int>& arr) {
    int i, j;
    for (i = 1; i < len; i++) {
        for (j = i - 1; j >= 0; j--) {
            if (arr[j] > arr[i]) {
                arr[j + 1] = arr[j];
            }
            else break;
        }
        arr[j + 1] = arr[i];
    }
}

void checkSort(vector<int>& arr) {
    int i, sorted;
    sorted = true;
    for (i = 0; i < len - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            sorted = false;
        }
        if (!sorted) {
            break;
        }
    }
    if (sorted) {
        cout << "정렬 완료" << endl;
    }
    else {
        cout << "정렬 오류" << endl;
    }
}

int main() {
    vector<int> vec = randomVector(len);
    auto start = chrono::high_resolution_clock::now();
    //InsertionSort(vec);
    //ShellSort1(vec);
    //ShellSort2(vec);
    ShellSort3(vec);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout << "Runtime: " << duration.count() << " seconds." << endl;
    checkSort(vec);
    return 0;
}
