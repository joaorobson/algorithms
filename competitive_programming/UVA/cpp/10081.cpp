
#include <stdio.h>
#include <cmath>
#include <iostream>
using namespace std;

#define datatype double
int main() {
    int k, n;

    while (cin >> k >> n) {
        datatype T[101][10];
        for (int j = 0; j <= k; j++)
            T[1][j] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                T[i][j] = T[i - 1][j];
                if (j < k)
                    T[i][j] += T[i - 1][j + 1];
                if (j > 0)
                    T[i][j] += T[i - 1][j - 1];
            }
        }
        datatype s = 0;
        for (int j = 0; j <= k; j++)
            s += T[n][j];
        double sol = s * 100.0 / pow(k + 1, n);
        printf("%.5f\n", sol);
    }

    return 0;
}
