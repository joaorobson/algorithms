#include <iostream>

using namespace std;


int main(){

    int c = 0,bn,b ,a;

    cin >> a;


        cin >> b;
    for(int i = 1;i<a;i++){
        cin >> bn;

        if(bn < b and c == 0){
          c = i+1;
        }
        b = bn;
   }
    cout <<  c <<endl;

}

