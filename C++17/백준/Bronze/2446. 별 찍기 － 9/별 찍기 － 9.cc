#include<iostream>
using namespace std;
//2445번 문제랑 거의비슷
int main() {
	int n;
	cin >> n;

	//위에부분 출력
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j < i; j++) {
			cout << " ";
		}
		//2445번 에서 for문 같은데에 = 추가
		for (int j = 0; j <= 2 * (n - i); j++) {
			cout << "*";
		}
		cout << "\n";
	}
	//아래부분 출력
	for (int i = n - 1; i > 0; i--) {
		for (int j = i; j > 1; j--) {
			cout << " ";
		}
		//2445번 에서 for문 같은데에 = 추가
		for (int j = 2 * (n - i); j>= 0; j--) {
			cout << "*";
		}
		cout << "\n";
	}
}