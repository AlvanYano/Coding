#include <iostream>
using namespace std;

int main(){

    cout << "Ini adalah program C++ pertama saya" << endl;
    
    cout << "Jurusan Teknik elektro" << endl;
    
    // menggunakan variabel
    int x = 10; // membuat var x tipe data integer diberi nilai 10

    float y = 10.345;

    cout << "nilai x = " << x << endl; 
    cout << "nilai y = " << y << endl; 

    string namamhs1 = "Alvan Fabiyano";

    cout << namamhs1 << endl;

    // menggunakan operator
    // *, / , + , -
    int z = 3;
    cout << "x % z = " << x % z << endl;

    // kondisional if ...
    // switch...case
    // menentukan sebuah angka genap atau ganjil : sisal hasil bagi, jika 1 ganjil dan 0 genap
    int angka = 19;
    if (angka % 2 == 1) cout << "angka ganjil" << endl;
    else cout << "angka genap" << endl;

    // menggunakan switch...case untuk konversi golongan ke gaji
    int golongan;

    cin >> golongan ;

    int gaji = 0; // nilai awal
    switch (golongan){
        case 1 : gaji = 1000000;
        break;
        case 2 : gaji = 2000000;
        break;
        case 3 : gaji = 3000000;
        break;
        case 4 : gaji = 4000000;
        break;
        default : gaji = 0;
    }

    cout << gaji << endl;
    
    return 0;
}