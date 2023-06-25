#include <iostream>
#include <chrono>
#include <vector>
#include <cmath>

#define len1 pow(2, 10)
#define len2 pow(2, 12)
#define len3 pow(2, 14)

using namespace std;

vector<int> randomVector(int n) {
    vector<int> vec(n);
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        vec[i] = rand() % 100; // Generating random integers between 0 to 100
    }
    return vec;
}

void maxHeapify(vector<int>& arr, int index, int heapSize) {
    int leftChildIndex = 2 * index + 1;
    int rightChildIndex = 2 * index + 2;

    int largestIndex = index;
    if (leftChildIndex<heapSize and arr[leftChildIndex]>arr[largestIndex]) {
        largestIndex = leftChildIndex;
    }
    if (rightChildIndex<heapSize and arr[rightChildIndex]>arr[largestIndex]) {
        largestIndex = rightChildIndex;
    }
    if (largestIndex != index) {
        swap(arr[index], arr[largestIndex]);
        maxHeapify(arr, largestIndex, heapSize);
    }
}

void minHeapify(vector<int>& arr, int index, int heapSize) {
    int leftChildIndex = 2 * index + 1;
    int rightChildIndex = 2 * index + 2;

    int smallestIndex = index;
    if (leftChildIndex<heapSize and arr[leftChildIndex]<arr[smallestIndex]) {
        smallestIndex = leftChildIndex;
    }
    if (rightChildIndex<heapSize and arr[rightChildIndex]<arr[smallestIndex]) {
        smallestIndex = rightChildIndex;
    }
    if (smallestIndex != index) {
        swap(arr[index], arr[smallestIndex]);
        minHeapify(arr, smallestIndex, heapSize);
    }
}

void buildMaxHeap(vector<int>& arr, int len) {
    for (int i = floor(len / 2); i >= 0; --i) {
        maxHeapify(arr, i, len);
    }
}

void buildMinHeap(vector<int>& arr, int len) {
    for (int i = floor(len / 2); i >= 0; --i) {
        minHeapify(arr, i, len);
    }
}

void maxHeapSort(vector<int>& arr, int len) {
    buildMaxHeap(arr, len);
    for (int i = len - 1; i >= 1; --i) {
        swap(arr[0], arr[i]);
        maxHeapify(arr, 0, i);
    }
}

void minHeapSort(vector<int>& arr, int len) {
    buildMinHeap(arr, len);
    for (int i = len - 1; i >= 1; --i) {
        swap(arr[0], arr[i]);
        minHeapify(arr, 0, i);
    }
}

void checkMaxHeapSort(vector<int>& arr, int len) {
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

void checkMinHeapSort(vector<int>& arr, int len) {
    int i, sorted;
    sorted = true;
    for (i = 0; i < len - 1; i++) {
        if (arr[i] < arr[i + 1]) {
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
    vector<int> vec1 = randomVector(len1);
    vector<int> vec2 = randomVector(len2);
    vector<int> vec3 = randomVector(len3);

    auto start1 = chrono::high_resolution_clock::now();
    //maxHeapSort(vec1, len1);
    minHeapSort(vec1, len1);
    auto end1 = chrono::high_resolution_clock::now();
    chrono::duration<double> duration1 = end1 - start1;
    cout << "n=2^10 Runtime: " << duration1.count() << " seconds." << endl;
    //checkMaxHeapSort(vec1, len1);
    checkMinHeapSort(vec1, len1);

    cout << endl;

    auto start2 = chrono::high_resolution_clock::now();
    //maxHeapSort(vec2, len2);
    minHeapSort(vec2, len2);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> duration2 = end2 - start2;
    cout << "n=2^12 Runtime: " << duration2.count() << " seconds." << endl;
    //checkMaxHeapSort(vec2, len2);
    checkMinHeapSort(vec2, len2);

    cout << endl;

    auto start3 = chrono::high_resolution_clock::now();
    //maxHeapSort(vec3, len3);
    minHeapSort(vec3, len3);
    auto end3 = chrono::high_resolution_clock::now();
    chrono::duration<double> duration3 = end3 - start3;
    cout << "n=2^14 Runtime: " << duration3.count() << " seconds." << endl;
    //checkMaxHeapSort(vec3, len3);
    checkMinHeapSort(vec3, len3);

    return 0;
}
