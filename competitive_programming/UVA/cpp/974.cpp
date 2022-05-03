#include <iostream>

using namespace std;

int main() {
    int n;
    int a, b;
    int v[40000];
    int divi = 0, dez = 1, rest = 0, cont = 0;
    for (int i = 2; i <= 40000; i++) {
        v[i] = 0;
    }
    for (int i = 2; i <= 40000; i++) {
        //  cout << v[i] << endl;
    }
    for (int i = 2; i <= 40000; i++) {
        int rt = i * i;
        divi = rt;
        dez = 1;
        while (divi > 0) {
            divi = rt / dez;
            rest = rt % dez;
            //  cout << i << " " << divi << " " <<  rest << " "<<divi + rest<<
            //  endl;
            if (divi > 0 && rest > 0 && divi + rest == i) {
                // cout << i << endl;
                //  cout << i << " " << divi << " " <<  rest << " "<<divi +
                //  rest<< endl;
                v[i] = i;
            }

            dez *= 10;
        }
    }

    cin >> n;

    int u = 1;
    while (n--) {
        cont = 0;
        cin >> a >> b;
        for (int i = a; i <= b; i++) {
            if (v[i] > 0) {
                cont++;
                if (cont == 1) {
                    cout << "case #" << u << endl;
                }
                cout << i << endl;
            }
        }
        if (cont == 0) {
            cout << "case #" << u << "\n"
                 << "no kaprekar numbers" << endl;
        }

        if (n > 0)
            cout << endl;
        u++;
    }
}
