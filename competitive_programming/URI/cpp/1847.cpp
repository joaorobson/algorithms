#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

int main(){

	int a,b,c;


  scanf("%d%d%d", &a, &b, &c);

	if(b < a && c >= b) cout << ":)"<< endl;
	else if(b > a && c <= b) cout << ":(" << endl;
	else if(b > a && c > b && abs(c- b) < abs(b - a)) cout << ":(" << endl;
	else if(b > a && c > b && abs(c - b) >= abs(b -a)) cout << ":)"<< endl;
	else if(b < a && c < b && abs(b - c) < abs(a - b)) cout << ":)"<< endl;
	else if(b < a && c < b && abs(b - c) >= abs(a - b)) cout << ":(" << endl;
	else if(a == b && c > b) cout << ":)" << endl;
	else if(a == b && c <= b) cout << ":(" << endl;
}
