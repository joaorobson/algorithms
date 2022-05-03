#include <math.h>
#include <stdio.h>
#include <iostream>
using namespace std;

double fat(long long n, long long k) {
    unsigned long long a = 1;
    double t = 0, sub = 0, mul = 0;
    for (long long i = 1; i <= n; i++) {
        t += log10(i);
        if (i == k) {
            mul = t;
        }
        if (i == (n - k)) {
            sub = t;
        }
    }
    return t - mul - sub;
}

int main() {
    unsigned long long n, k;
    while (cin >> n >> k) {
        printf("%d\n", int(fat(n, k)) + 1);
    }
}
