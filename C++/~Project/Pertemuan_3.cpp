#include <iostream>

using namespace std;

int main(){
 
    int golongan_179;
    int gaji_179;

    cout << "Masukan Golongan : ";

    cin >> golongan_179;

    switch (golongan_179) {
        case 1:
            gaji_179 = 1000000;
            break;
        case 2:
            gaji_179 = 2000000;
            break;
        case 3:
            gaji_179 = 3000000;
            break;
        case 4:
            gaji_179 = 4000000;
            break;  
        default:
            gaji_179 = 0;
    }

    cout << "Gaji Anda : " << gaji_179 << endl;

    // perulangan / looping
    for (int i = 0; i < 10; i++){
        cout << "Teknik Elektro " << i << endl;
    }

    // menghitung faktorial
    // n! = 1*2*3*4*5*6*7*8*9*10

    int n_179;

    cout << "Masukan n : ";

    cin >> n_179;
    int hasil_179 = 1;
    for (int i = 1; i <= n_179; i++){
        hasil_179 *= i;
    }

    cout << "Hasil faktorial dari " << n_179 << " adalah " << hasil_179 << endl;

    // loop untuk menampilkan matriks 
    // 1 2
    // 3 4

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            cout << i * 2 + j + 1 << " ";
        }
        cout << endl;
    }

    int angka_179[4] = {10, 20, 30, 40};

    // menampilkan isi array
    cout << "Isi array pertama : " << angka_179[0] << endl;
    cout << "Isi array kedua : " << angka_179[1] << endl;
    cout << "Isi array ketiga : " << angka_179[2] << endl;
    cout << "Isi array keempat : " << angka_179[3] << endl;

    cout << endl;

    for (int i = 0; i < 4; i++){
        cout << "Isi array ke-" << i + 1 << " : " << angka_179[i] << endl;

    }

    string buah_179[6] = {"Apel", "Anggur", "Semangka", "Durian", "Rambutan", "Mangga"};

    for (int i = 0; i < 6; i++){
        cout << "Buah ke-" << i + 1 << " : " << buah_179[i] << endl;
    }

    return 0;

}