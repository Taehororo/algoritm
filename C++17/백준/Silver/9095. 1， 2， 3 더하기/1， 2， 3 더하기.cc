#include<iostream>
#include<vector>
using namespace std;
int d[1001];
int main() {
	int t;
	vector<int> n;
	cin >> t;
	d[1] = 1;
	d[2] = 2;
	d[3] = 4;
	for (int i = 4; i <= 11; i++) {
		d[i] = d[i - 3] + d[i - 2] + d[i - 1];
	}
	for (int i = 0; i < t; i++) {
		int x;
		cin >> x;
		n.push_back(x);
	}
	for (int i = 0; i < n.size(); i++) {
		cout << d[n[i]] << endl;
	}
}