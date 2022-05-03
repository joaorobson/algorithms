#include <math.h>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

bool is_p(int a) {
    if (a == 2 or a == 1) {
        return true;
    }
    if (a % 2 == 0) {
        return false;
    }

    for (int i = 3; i <= sqrt(a); i += 2) {
        if (a % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int a, c, t;

    while (cin >> a >> c) {
        vector<int> b;
        for (int i = 1; i <= a; i++) {
            if (is_p(i)) {
                b.push_back(i);
            }
        }
        int in;
        if (b.size() & 1) {
            t = 2 * c - 1;
            in = (b.size() - t) / 2;
        } else {
            t = 2 * c;
            in = (b.size() - t) / 2;
        }
        if (t >= b.size()) {
            t = b.size();
            in = 0;
        }

        cout << a << " " << c << ":";
        for (int i = in; i < in + t; i++) {
            cout << " " << b[i];
        }
        cout << endl;
        cout << endl;
        t = 0;
    }
}
