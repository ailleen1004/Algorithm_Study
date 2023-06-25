#include <iostream>
#include<cstdio>
#include <ctime>
#define n 200 // 10, 50, 100, 150, 200

using namespace std;

int main(){
	clock_t start, end; // 소요 시간 측정

	// nxn array a, b, c & a*b=ab, ans1*c=abc
	int a[n][n];
	int b[n][n];
	int c[n][n];
	int ab[n][n];
	int abc[n][n];

	//array 계산할 값 할당
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			a[i][j] = 2;
		}
	}
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			b[i][j] = 3;
		}
	}
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			c[i][j] = 4;
		}
	}

	start = clock(); // cubic complexity 계산 start

	//3중 for loop 1. array a*array b = array ab
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			int ans = 0;
			for (int k = 0; k < n; k++){
				ans += a[i][k] * b[k][j];
			}
			ab[i][j] = ans;
		}
	}

	//3중 for loop 2. array ab*array c = array abc 
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			int ans = 0;
			for (int k = 0; k < n; k++){
				ans += ab[i][k] * c[k][j];
			}
			abc[i][j] = ans;
			cout << "abc[" << i << "][" << j << "] = " << abc[i][j] << endl;
		}
	}

	end = clock(); // cubic complexity 계산 end

	cout << (double)(end - start) << "ms" << endl;

	return 0;
}