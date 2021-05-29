#include <iostream>

using namespace std;

int main(){

  int a;
  while(cin >> a){
    int m[a][a];
    int pos = a/3;
    for(int i = 0;i < a;i++){
      for(int j = 0;j < a;j++){
        if(i == j && (i < pos || i > a - pos - 1)){
          cout << 2;
        }
        else if(i + j == a - 1 && (i < pos ||  i > a - pos - 1)){
            cout << 3;
        }
        else if(i >= pos && i <= a - pos - 1 && j  >= pos && j <= a - pos - 1){
          if(i == a/2 && j == a/2){
            cout << 4;
          }else{
          cout << 1;}
        }
        else{
          cout << 0;
        }




      }
      cout << endl;
    }
    cout << endl;


  }

}
