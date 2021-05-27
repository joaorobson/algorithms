#include <iostream>

using namespace std;

int main(){

  int a,b;
  cin >> a;

  while(a--){
    cin >> b;
    if(b & 1){
      cout << 1 << endl;
    }else{
      cout << 0 << endl;
    }


  }

}
