#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
struct myclass {
	  bool operator() (int i,int j) { return (i<j);}
} myobject;

int main(){

	int a, c = 0;
	long int t;
	vector <long int> b;

	cin >> a;

	for(int i = 0;i<a;i++){
		cin >> t;
		while(find(b.begin(), b.end(),t) != b.end()){
			t++;
			c++;
		}
		b.push_back(t);

	
	}
	cout << c << endl;

}

