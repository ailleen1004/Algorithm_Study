#include "sorting.h"

void sort(std::vector<int>& arr);
void quicksort(std::vector<int>& arr, int left, int right);
int partition(std::vector<int>& arr, int left, int right, int pivotIndex);

void sort(std::vector<int>& arr) {
    quicksort(arr, 0, arr.size() - 1);
}

void quicksort(std::vector<int>& arr, int left, int right) {
    if (left < right)
    {
        int pivotIndex = (left + right) / 2;
        pivotIndex = partition(arr, left, right, pivotIndex);
        quicksort(arr, left, pivotIndex - 1);
        quicksort(arr, pivotIndex + 1, right);
    }
}

int partition(std::vector<int>& arr, int left, int right, int pivotIndex) {
    int pivotValue = arr[pivotIndex];
    int storeIndex = left;

    int temp = arr[pivotIndex];
    arr[pivotIndex] = arr[right];
    arr[right] = temp;

    for (int j = left; j < right; j++)
    {
        if (arr[j] < pivotValue)
        {
            temp = arr[storeIndex];
            arr[storeIndex] = arr[j];
            arr[j] = temp;
            storeIndex++;
        }
    }
    temp = arr[storeIndex];
    arr[storeIndex] = arr[right];
    arr[right] = temp;
    return (storeIndex);
}

