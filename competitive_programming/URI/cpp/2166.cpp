#include <iostream>
#include <iomanip>


using namespace std;


int main(){


    double a = 1;
    
    int b;
    double den = 1;
    cin >> b;
    if(b == 0){
      
      cout << fixed << setprecision(10) << den << endl; 
    }else{
    den = 2;
    for(int i =1;i < b;i++){

        den = 2 + 1/den;

    }
      cout << fixed << setprecision(10) <<1+1/den << endl; 
   }


}
