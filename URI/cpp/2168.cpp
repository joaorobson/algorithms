#include <iostream>

using namespace std;


int main(){


  int k= 0,l=0,co=0, co2 = 0,li=0,c= 0,a;

  cin >> a;
    

  int m[a+1][a+1];
  char r[a][a]; 


  for(int i = 0;i < a+1;i++){
    for(int j = 0;j<a+1;j++){

      cin >> m[i][j];

    }}


  for(int i = 0;i <a;i++){
    for(int j = 1;j<a+1;j++){
       if(j == 1){
         co = m[i][j-1] + m[i+1][j-1];
       }
       co2 = m[i][j] + m[i+1][j];
       
       if(co+co2 >= 2){
        r[k][l] = 'S'; 
       }
       else{
        r[k][l] = 'U'; 
       }
        co = co2;
        l++;
    }
    k++;
    l = 0;
  
  }

  for(int i = 0;i < a;i++){
    for(int j = 0;j<a;j++){

      cout  << r[i][j];

    }cout << endl;}
}
