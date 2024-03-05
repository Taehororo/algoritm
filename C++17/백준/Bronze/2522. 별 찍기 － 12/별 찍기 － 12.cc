#include<iostream>
using namespace std;

int main() {
	int n;
	cin >> n;

	//위에부분 출력
	for (int i = 1; i <=n; i++) {
		for (int j = n; j > i; j--) {
			cout << " ";
		}
		for (int j = 0; j < i; j++) {
			cout << "*";
		}
		cout << "\n";
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			cout << " ";
		}
		for (int j = n; j > i; j--) {
			cout << "*";
		}
		cout << "\n";
	}
}