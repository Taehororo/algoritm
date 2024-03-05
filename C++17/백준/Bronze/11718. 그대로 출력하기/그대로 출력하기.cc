#include<iostream>
#include<string>
using namespace std;
int main()
{
	string t;
	while (1) {
		getline(cin, t);
		if (t == "") {
			break;
		}
		cout << t << "\n";
	}
}
