#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int k = N - 1; k > i; k--) {
			cout << " ";
		}
		if (i == 0) {
			cout << "*";
		}
		else if (i == N - 1) {
			for (int j = 0; j < 2 * N - 1; j++)
				cout << "*";
		}
		else {
			cout << "*";
			for (int j = 0; j < i * 2 - 1; j++) {
				cout << " ";
			}
			cout << "*";
		}
		cout << endl;
	}
	return 0;
}