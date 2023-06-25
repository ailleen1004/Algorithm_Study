#include <iostream>
#include<cstdio>
#include <ctime>
#define n 30 //10, 20, 30

using namespace std;

int fibo(int);

int main() {
	clock_t start, end; // �ҿ� �ð� ����
	int a = 1;
	int b = 1;

	start = clock(); // cubic complexity ��� start

	for (int i = 1; i < n; i++) {
		cout << fibo(i) <<" ";
	}

	end = clock(); // cubic complexity ��� end

	cout << endl << (double)(end - start) << "ms" << endl;

	return 0;
}

int fibo(int x) {
	if (x <= 2) {
		return 1;
	}
	else {
		return fibo(x - 1) + fibo(x - 2);
	}
}