#include <bits/stdc++.h>

using namespace std;

vector<unsigned long long> factors(unsigned long long n){
  vector<unsigned long long> v;
  while(not n%2){
    n /= 2;
    v.push_back(2);
  }

  for(long long int i =3;i <= sqrt(n) + 1;i = i +2){
    while(n%i == 0){
      n /= i;
      v.push_back(i);
    }
  } 
  v.push_back(n);
  return v;

}

int main(){
  
  unsigned long long n;

  cin >> n;
  while(n){
    vector<unsigned long long> v = factors(n);
    cout << n << " = ";
    int k = 0;
    for(auto i:v){
      cout << i << (k == (v.size() - 1) ? "\n" : " x ");
      k++;
    }
    cin >> n;
  }

}
