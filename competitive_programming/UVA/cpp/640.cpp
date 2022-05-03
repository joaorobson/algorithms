#include <bitset>
#include <cmath>
#include <iostream>

using namespace std;

int main() {
    bitset<1000002> v;

    long long int vet[100];
    int num = 10, dez = 1;
    int rest = 0;
    for (int i = 1; i <= 1000000; i++) {
        num = i;
        rest = num;
        int logn = log10(num);
        int dez = pow(10, logn);
        while (dez > 0) {
            // cout << num << " " << rest << " "<< dez<<endl;
            num = rest / dez + num;
            rest = rest % dez;

            dez /= 10;
        }
        // cout << num << endl;
        v[num] = 1;
    }

    for (int i = 1; i <= 1000000; i++) {
        if (v[i] == 0) {
            cout << i << endl;
        }
    }
}
