#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

	int a,b,c, k = 1;
	vector<int> v;
	vector<int>::iterator it;
	cin >> a >> b;

	while(a != 0 && b != 0){
		for(int i = 0;i < a;i++){
			cin >> c;
			v.push_back(c);
		}
		sort(v.begin(), v.end());

		cout << "CASE# " << k << ":" << endl;
		for(int i = 0;i < b;i++){
			cin >> c;
			it = find(v.begin(), v.end(), c);
			if(it != v.end()){
				cout << c << " found at " << it - v.begin()+ 1  << endl;
			}
			else{
				cout << c << " not found" << endl;
		
			}
		}


		k++;
		cin >> a >> b;
		v.clear();
	}



}
