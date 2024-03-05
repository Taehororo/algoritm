#include<iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	//위에부분 출력
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			cout << "*";
		}
		for (int j = 0; j < 2*(n - i);j++ ) {
			cout << " ";
		}
		for (int j = 0; j < i; j++) {
			cout << "*";
		}
		cout << "\n";
	}
	//아래부분 출력
	for (int i = n-1; i >0; i--) {
		for (int j = i; j >0; j--) {
			cout << "*";
		}
		for (int j = 2 * (n - i); j > 0;j--) {
			cout << " ";
		}
		for (int j = i; j > 0; j--) {
			cout << "*";
		}
		cout << "\n";
	}
}