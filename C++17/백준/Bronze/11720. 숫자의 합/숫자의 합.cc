#include<iostream>
#include<string>
using namespace std;
int main()
{
	int n;
	cin >> n;
	int hap = 0;
	string s;
	cin >> s;
	for (int i = 0; i < n; i++) {
		hap += s[i] - '0';
	}
	
	cout << hap;
}

