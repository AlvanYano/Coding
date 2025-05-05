#include <iostream>
using namespace std;

union Data {
    int i;
    float f;
    char c;
};

int main() {
    Data data;

    data.i = 10;
    cout << "data.i = " << data.i << endl;

    data.f = 3.14;  // Sekarang kita isi data.f
    cout << "data.f = " << data.f << endl;

    // mencoba mengakses data i
    cout << data.i << endl;

    data.c = 'A';   // Sekarang kita isi data.c
    cout << "data.c = " << data.c << endl;

    // Sekarang nilai data.i dan data.f kemungkinan besar sudah rusak
    cout << "data.i (setelah data.c) = " << data.i << endl;

    return 0;
}
