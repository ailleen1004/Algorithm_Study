#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

vector<int> randomVector(int n) {
	vector<int> vec(n);
	srand(time(NULL));
	for (int i = 0; i < n; i++) {
		vec[i] = rand() % 100; // Generating random integers between 0 to 99
	}
	return vec;
}

void bubbleSort(vector<int>& arr, int n) {
	int temp = 0;
	for (int i = 0; i < n - 1; i++) {
		for (int j = i; j < n; j++) {
			if (arr[j] < arr[i]) {
				temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
	}
}

int main() {
	double tic, toc;
	for (int n : {50, 100, 150, 200, 250}) {
		vector<int> vec = randomVector(n);
		cout << "Random Vector: ";
		for (int i = 0; i < n; i++) {
			cout << vec[i] << " "; // Printing the generated vector
		}
		tic = clock();
		bubbleSort(vec, n);
		toc = clock();
		cout << "\nSorted Vector: ";
		for (int i = 0; i < n; i++) {
			cout << vec[i] << " "; // Printing the sorted vector
		}
		cout << endl << n << ": " << toc - tic << "ms" << endl << endl;
	}
	return 0;
}
