#include<iostream>
#include<vector>
using namespace std;
int d[101][10] = { 0 };
int main() {
	int n;
	cin >> n;

	for (int i = 1; i < 10; i++) {
		d[1][i] = 1;
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			if (j == 0) {
				d[i][j] = d[i - 1][j + 1];
			}
			else if (j == 9) {
				d[i][j] = d[i - 1][j - 1];
			}
			else {
				d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1];
			}
			d[i][j] %= 1000000000;
		}
	}
	int cnt = 0;
	for (int i = 0; i < 10; i++) {
		cnt = (cnt + d[n][i]) % 1000000000;
	}
	cout << cnt;

}