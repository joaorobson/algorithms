#include <iostream>
#include <algorithm>

#include <vector>
#include <bitset>
#include <stdio.h>

using namespace std;

int main(){


  long long cont_tot= 0,cont_rou=0,ant,o,a,i = 0;
  vector <long long> t,k;
  long long b,num,soma=0;
  cin >> a;
	o = a;


  while(o--){

    cin >>b;
    t.push_back(b);
    i++;
	

  }
  bitset<1000000> foo;
  i = 0;
  k.push_back(0);
  while(true){
    if(i < 0 || i >= t.size() || t[i] == 0){
      break;
    }
    else{
      num = t[i];
      t[i]--;
      foo.set(i,1);
      if(num&1){
        i++;
      }
      else{
        i--;
      }

   }

  


  }
  for(auto& p: t){
    soma += p;
  }
  o = a;
  i = 0;
    cout << foo.count() << ' ' <<  soma<<endl;
    i++;
}
