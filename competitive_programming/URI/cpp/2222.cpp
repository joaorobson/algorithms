#include <iostream>
#include <vector>
#include <set>
#include <algorithm>    // std::set_intersection, std::sort
#include <iterator>
#include <bitset>





using namespace std;

int intersection(vector<int> a, vector<int> b){
  set <int, greater <int> > res;

  if( a.size() > b.size()){
    for(const int& i : a ){
      for(int k = 0; k < b.size();k++){
        if( b[k] == i){
          res.insert(i);
        }
      }
    }
  }else{
  for(const int& i : b ){
      for(int k = 0; k < a.size();k++){
        if( a[k] == i){
          res.insert(i);
        }
    }
  }
  }
  return res.size();
}

int union_(vector<int> a, vector<int> b){
  set <int, greater <int> > res;
  for(const int& i : a ){
    res.insert(i);
	}
  for(const int&l: b) {
    res.insert(l);
  }
  return res.size();
}
int main() {

    //reading an integer
      int a = 0;
      cin >> a; 
      for(int i = 0;i < a;i++) {
        int b,c,d,f,g,h;
        int e,s,k,j ;
        vector<bitset<61>> m;


        cin >>b;
        for(k =0;k < b;k++) {
          bitset<61> p;
          cin >> c;
          for(j=0; j < c;j++){
            cin >> d;
            p[d] = 1;
          }
          m.push_back(p);
        }
        cin >> e;
      for(s=0; s < e;s++){
        cin >> f;
        cin >> g;
        cin >> h;
        if( f == 1){
          cout << (m[g-1] & m[h-1]).count() << endl;
        }else{
          cout << (m[g-1] | m[h-1]).count() << endl;
        }
      }
  }
}
