#include <iostream>


using namespace std;


int main(){

  int a,b,m2,m3,m4,m5;

  cin >> a;


  for(int i = 0; i < a;i++){


    cin >> b;
    
    if(b%2==0) m2++;
    if(b%3==0) m3++;
    if(b%4==0) m4++;
    if(b%5==0) m5++;

  }


  cout << m2 << " Multiplo(s) de 2" << endl;
  cout << m3 << " Multiplo(s) de 3" << endl;
  cout << m4 << " Multiplo(s) de 4" << endl;
  cout << m5 << " Multiplo(s) de 5" << endl;
}
