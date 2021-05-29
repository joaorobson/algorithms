#include <iostream>

using namespace std;

int main(){

  int n,a,b;

  while(cin >> n){
    b = n - 1;
    a = 0;
    for(int i = 0;i < n;i++){
      for(int j = 0;j < n;j++){
        if(i == a && j == b){
          cout << 2;
          a++;
          b--;
        }
        else if(i == j){
          cout << 1;
        }
        else{
          cout << 3;
        }
      }
      cout << endl;
    }
  }
}
