#include <bits/stdc++.h>

using namespace std;

int main(){
  int a;
  cin >> a;
  while(a){
    int b;
    deque<int> s;
    vector<int> v;
    for(int i = 1; i<=a;i++){
      s.push_back(i);
    }

    while(s.size() > 1){
      b = s.front();
      s.pop_front();
      v.push_back(b);
      b = s.front(); 
      s.pop_front();
      s.push_back(b);
    }

    cout << "Discarded cards:" << (v.size() == 0 ? "\n" : " ");
    auto i = 0;
    for(auto a:v){
      cout << a << (i == v.size() - 1 ? "\n" : ", ");
      i++;
    }
    cout << "Remaining card: " << s.front() << endl;
    cin >> a;
  }
}
