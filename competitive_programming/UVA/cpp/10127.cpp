#include <iostream>

using namespace std;

int main() {
    unsigned long long i, resto;
    unsigned long long a;

    while (cin >> a) {
        int cont = 1;

        int i = 1;

        resto = i % a;
        if (resto != 0) {
            while (1) {
                resto *= 10;
                resto = resto % a;

                if (resto == 0) {
                    break;
                }
                resto++;
                cont++;
            }
        }
        cout << cont << endl;
    }
}
