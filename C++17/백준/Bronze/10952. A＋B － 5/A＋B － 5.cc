#include<iostream>
using namespace std;
int main()
{
	int a, b;
	int cnt = 0;
	while (1) {
		cin >> a >> b;
		if (a == 0 || b == 0) return 0;
		cout << a + b << endl;
	}
		
}
