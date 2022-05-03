#include <cmath>
#include <iostream>
using namespace std;
int main() {
    int a;
    cin >> a;
    while (a) {
        long long b;
        cin >> b;
        b < 0 ? b = -b : b;
        int sub;
        long long inf = 0;
        long long sup = 4 * b;
        long long mid = 0;
        long long n = 0;
        while (1) {
            if (b == 0) {
                mid = 3;
                break;
            } else {
                mid = ceil((inf + sup) / 2.0);
                n = mid * (mid + 1) / 2;
                sub = int(n - b);
                // cout << "inf: " << inf << " mid: " <<mid << " sup:
                // "<<sup<<endl;
                if (inf == sup - 1 or n == b) {
                    break;
                } else if (n > b) {
                    sup = mid;
                } else if (n < b) {
                    inf = mid;
                }
                // cout << sub << " " <<mid<< endl;
            }
        }
        while (sub % 2 != 0 || sub < 0) {
            mid += 1;
            n = mid * (mid + 1) / 2;
            sub = (n - b);
            // cout << "aaa" <<sub << endl;
        }
        cout << mid << endl;

        if (a > 1) {
            cout << endl;
        }

        a--;
    }
}
