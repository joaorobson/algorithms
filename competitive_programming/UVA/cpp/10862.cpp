#include <iostream>

using namespace std;

long long fat(long long unsigned n) {
    int cont = n, i = n;
    long long fat = 1;

    while (cont--) {
        fat = fat * i;
        i--;
    }
    return fat;
}

int main() {
    long long unsigned a;
    cin >> a;

    while (a > 0) {
        if (a == 1) {
            cout << 1 << endl;
        } else {
            cout << fat(a + 1) / a << endl;
        }

        cin >> a;
    }
}
