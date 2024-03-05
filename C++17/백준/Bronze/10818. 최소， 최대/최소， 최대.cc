#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int n;
	cin >> n;
	int x;
	int a[1000001];
	
	for (int i = 0; i < n; i++) {
		cin >> x;
		a[i] = x;
	}
	sort(a, a+n);

	cout << a[0] << " " << a[n - 1];
}

