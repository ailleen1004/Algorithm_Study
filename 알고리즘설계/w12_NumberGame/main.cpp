#include <iostream>

using namespace std;

int main() {
	int array[8][9] = {
		{ 3, 4, 9, -2, 2, 51, -23, 2, -1},
		{ 223,7,8,-11,5, -99,2,3, -4 },
		{ 2,51,-23, -23,6,3,2,4,5 },
		{ 5,-99,2,-1,32,2,5,-99,2 },
		{ 6,3,3,-4,2,-1,6,3,3 },
		{ 32,2,4,5,3,-4,2,-1,4 },
		{ 4,4,23,6,2,-1,3,-4,34 },
		{ 78,32,1,7,3,-4,-23,-23,6 },
	};

	int result[9][9] = { 0 }; // sum�� ������ ��� �� ������ 9*9 result �迭

	for (int i = 0; i < 9; i++) {
		result[i][1] = array[0][i]; // 0��° �࿡�� ������� ������ ����
		result[i][0] += result[i][1];
		int n = i; // �� index
		for (int j = 1; j < 8; ++j) {
			if (n == 0) { // index�� �� ����(0 ��°)�� ���� �� : ���� �밢�� ���� �������� ����
				result[i][j + 1] = max(array[j][n], array[j][n + 1]);
				if (result[i][j + 1] == array[j][n + 1]) {
					n = n + 1;
				}
			}
			else if (n > 0 and n!=8) { // index�� 1~7��°�� ���� �� : ���� �밢�� �� ��� ����
				result[i][j + 1] = max(max(array[j][n], array[j][n + 1]), array[j][n-1]);
				if (result[i][j + 1] == array[j][n + 1]) {
					n = n + 1;
				}
				else if (result[i][j + 1] == array[j][n - 1]) {
					n = n - 1;
				}
			}
			else if (n == 8) { // index�� �� ������(8 ��°)�� ���� �� : ������ �밢�� ���� �������� ����
				result[i][j + 1] = max(array[j][n], array[j][n - 1]);
				if (result[i][j + 1] == array[j][n - 1]) {
					n = n - 1;
				}
			}
			result[i][0] += result[i][j + 1];
		}
	}

	/* sum & result ��� ���
	sum1 : 402 / { 3, 223, 51, 5, 6, 32, 4, 78, }
	sum2 : 403 / { 4, 223, 51, 5, 6, 32, 4, 78, }
	sum3 : 193 / { 9, 8, 51, 5, 6, 32, 4, 78, }
	sum4 : 182 / { -2, 8, 51, 5, 6, 32, 4, 78, }
	sum5 : 107 / { 2, 5, 6, 32, 2, 5, 23, 32, }
	sum6 : 156 / { 51, 5, 6, 32, 2, 5, 23, 32, }
	sum7 : 34 / { -23, 3, 5, 2, 3, 4, 34, 6, }
	sum8 : 59 / { 2, 3, 5, 2, 3, 4, 34, 6, }
	sum9 : 56 / { -1, 3, 5, 2, 3, 4, 34, 6, }
	*/

	int max = result[0][0];
	int index = 0;
	for (int i = 1; i < 9; i++) { // 2���� �迭 ���� �� �迭����, 0��° index�� ��θ� ������ ������ ���� �����
		if (max < result[i][0]) { // ���Ͽ� ���� max �� ��� ����� index�� ã��
			max = result[i][0];
			index = i;
		}
	}

	// ���
	cout << "Max : " << max << endl;
	cout << "Route : " << endl;
	cout << "{ ";
	for (int i = 1; i < 8; i++) {
		cout << result[index][i] << ", ";
	}
	cout << result[index][8] << " }";
}
