#include <bits/stdc++.h>

using namespace std;

int main(){


  int a, b, cheg, sa, es = -1;

  cin >> a;

  while(a){
    stack<int> s, chega, est;
    queue<int> sai, ans;
    es = -1;
    int cheg, sa;
    for(int i = a;i>=1;i--){
      chega.push(i);
    }
    for(int i=1;i <= a;i++){
      cin >> b;
      if(!b){
        break;
      }
      sai.push(b);
    }
    while(1 && b){
      if(chega.size()){
        cheg = chega.top();
      }
      sa = sai.front();
      if(est.size()){
        es = est.top();
      }
      //cout << "oi "  << cheg << " " << sa << " " << es << endl;
      if(ans.size() == a){
        cout << "Yes" << endl;
        break;

      }

      if(chega.size() == 1 && cheg != sa && es != sa){
        cout << "No" << endl;
        break;
      }
      if(chega.size() == 0 && es != sa){
        cout << "No" << endl;
        break;
      }
      if(cheg == sa){
        ans.push(sa);
        chega.pop();
        sai.pop();
      }
      else if(es == sa){
        ans.push(sa);
        est.pop();
        sai.pop();

      }
      else{
        est.push(cheg);
        chega.pop();
      }
    }
    if(!b){
      cout << endl;
      cin >> a;
    }
  }

}
