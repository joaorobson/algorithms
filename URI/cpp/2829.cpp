#include <bits/stdc++.h>

using namespace std;

class myComparator 
{ 
public: 
    int operator() (const string& p1, const string& p2) 
    {
      if(p1.tolower() == p2.tolower()){
      if( std::all_of( p1.begin(), p1.end(), &::islower )) { // all lowercase
        return p1 > p2; 
      }else{
        return p1 < p2; 
      }
    } 
    return p1 < p2;
    }
}; 



int main(){
  
  priority_queue <string, vector<string>, greater<string>> q;
  int a;

  cin >> a;
  string s;
  for(int i =0;i<a;i++){
    cin >> s;
    q.push(s);
  }

  while(not q.empty()){
    auto i = q.top();
    q.pop();
    cout << i << endl;
  }

}
