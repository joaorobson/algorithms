#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main(){

  int a, b, c,i=0;
  string n1,n2,n3,n4;
  char *pont;
  cin >> a;

  while(a--){
    cin >> n1 >> n2 >> n3 >> n4;
    cin >> b >> c;

    if((b+c)&1){
      if(n2 == "IMPAR"){
        cout << n1 << endl;
      }
      else{
        cout << n3 << endl;
      }

    }
    else{
      if(n2 == "PAR"){
        cout << n1 << endl;
      }
      else{
        cout << n3 << endl;
      }

    }




  }

}
