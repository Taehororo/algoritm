#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T, a, b;
	char c;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> a >> c >> b;
		cout << a + b << "\n";
	}

}