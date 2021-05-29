#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main(){

  int a, d = 1;
  string b,c;
  cin >> a;
  cin.ignore();

  while(a--){
    cin >> b >> c;
    if(b == c)cout <<  "Caso #" << d << ": De novo!" << endl;
    else if(b == "tesoura" && c == "papel")cout << "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "tesoura" && c == "lagarto")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "papel" && c == "pedra")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "papel" && c == "Spock")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "pedra"&& c == "lagarto")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "pedra" && c == "tesoura")cout << "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "lagarto" && c == "Spock")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "lagarto" && c == "papel")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "Spock" && c == "tesoura")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else if(b == "Spock" && c == "pedra")cout <<  "Caso #" << d << ": Bazinga!" << endl;
    else cout <<  "Caso #" << d << ": Raj trapaceou!" << endl;

    d++;

  }




}
