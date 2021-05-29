#include <iostream>

using namespace std;

int main(){
  int num;
  while(1){
    cin >> num;
    if(num == 0){
      break;
    }
    int m[num][num],dois = 1,aux = 1,maior = 1;


    for(int i = 0;i < num;i++){
      for(int j = 0;j < num;j++){
        m[i][j] = dois;
        if(dois > maior){
          maior = dois;
        }
        dois *= 2;



      }
      aux *= 2;
      dois = aux;


    }
    int f = maior;
    int dig = 0;

    while(f != 0){
      f /= 10;
      dig++;
    }
    for(int i = 0;i < num;i++){
      for(int j = 0;j < num;j++){
        cout.width(dig);cout <<right<< m[i][j];
        if(j < num - 1){
          cout << " ";
        }
      }
      cout << endl;
    }
cout << endl;


  }
}
