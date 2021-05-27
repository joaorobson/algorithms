#include <iostream>
#include <string.h>
#include <string>

using namespace std;
int main() {
  string blink;
  int num = 4, soma = 0;
  for (int i = 0; i < 3; i++) {
    getline(cin, blink);

    while (strcmp(blink.c_str(), "caw caw") != 0) {
      for (int j = 0; j < 3; j++) {
        if (blink[j] == '*') {
          soma += num;
          if (soma > 1000) {
            soma -= num;
            break;
          }
        }
        num /= 2;
      }
      getline(cin, blink);
      num = 4;
    }
    cout << soma << endl;
    soma = 0;
  }
}
