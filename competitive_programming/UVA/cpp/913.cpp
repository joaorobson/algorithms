#include <iostream>

using namespace std;

int main() {
    long long odd = 1;
    long long n, six = 6;
    long long aux = 6;
    while (cin >> n) {
        odd = 7;
        if (n == 1) {
            cout << 1 << endl;
        } else if (n == 3) {
            cout << 15 << endl;
        } else {
            for (int i = 3; i < n; i += 2) {
                aux = aux + 4;
                odd = odd + aux;
            }
            aux = 6;
            cout << odd + odd - 2 + odd - 4 << endl;
        }
    }
}
