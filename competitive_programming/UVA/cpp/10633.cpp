#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
long long gcd(long long a, long long b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    /*m = n - d/10
    n - m =  n - (n-d/10)
    n-m = 10n - n + d/10
    n - m = 9n +d/10
     18 = 9n + d/10
    10*x = 9N + d
    */
    unsigned long long a, f = 0;
    scanf("%llu", &a);
    while (a != 0) {
        vector<unsigned long long int> r;
        for (long long int i = 9; i >= 0; i--) {
            if ((10 * a - i) % 9 == 0) {
                r.push_back((10 * a - i) / 9);
            }
        }
        int k;
        for (k = 0; k < r.size() - 1; k++) {
            cout << r[k] << " ";
        }
        cout << r[k] << endl;
        cin >> a;
    }
}
