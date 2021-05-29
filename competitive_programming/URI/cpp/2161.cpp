#include <iostream>
#include <iomanip>

using namespace std;

int main() {

  double a = 3;

  double b = 1/6;

  int c;
  cin >> c;
  for(int p = 0;p < c;p++){
    b = 1/(6 + b);


  }
 
   cout << fixed << setprecision(10) << 3 +b<< endl;

}
