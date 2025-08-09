#include <iostream>

using namespace std;

int main(){

    
    int a, b, hasil;

    cout << "Msukan nilai "; cin >> a;;
    cout << "Masukan nilai kedua ";cin >> b;
    hasil = a + b;
    cout << "Hasil Penambahan " << hasil << endl;
    hasil = a * b;
    cout << "Hasil Perkalian " << hasil<< endl;
    
    #ifdef a
    //  tipe data float
    int suhu;
    float f, r, k;
    cout << "Masukan Suhu dalam Celcius "; cin >> suhu;
    f = (9.5 *suhu ) +32; r = 0.8 *suhu;k = 273 + suhu;
    cout << "Hasil Konversi Suhu: " << endl;
    cout << "Suhu dalam Fahrenhait: " << f << endl;
    cout << "Kelvin: " << k << " Reamur: " << r << endl;
    
    
    string nama; int umur;bool pilihan;
    cout << "Masukan nama Anda : "; cin >> nama;
    cout << "Perkenalkan, nama saya " << nama<< endl;
    cout << "Masukan umurmu : "; cin >> umur;
    pilihan = umur > 18;
    cout << "Anda sudah dewasa : " << pilihan << endl;
    
    
    // char
    string nama3;
    cout << "Masukan nama anda "; cin >> nama3;
    char nama1 = nama3[0];
    char nama2 = nama3[1];
    cout << "Huruf pertama namamu adalah " << nama1 << endl;
    cout << "Huruf kedua namamu adalah " << nama2 << endl;
    

    
    //boolean
    bool nilai = false;
    cout << nilai << endl;
    

    
    // kondisional 
    int umur1;
    cout << "Masukan umurmu : "; cin >> umur1;

    if (umur1 < 18) {
        cout << "Anda belum dewasa";
    
    } else if(umur1>= 18 && umur1 < 60){
        cout << "Anda sudah tua";
    } else {
        cout << "Anda sudah tua";
    }
    
    
    
    int kode;

    cout << "Masukan kode jurusan :"; cin >> kode;

    switch (kode)
    {
    case 1:
        cout << "Teknik elektro";
        break;
    case 2:
        cout << "Teknik komputer";
        break;
    case 3:
        cout << "Teknik informatika";
        break;
    default:
        cout << "Masukan tidak valid";
    }
    
    

    
    // Perulangan 
    // For loop

    for(int i = 0; i < 10; i++){
        cout << i << " " ;
    }
    
    
    // while
    int ii = 0;
    while (ii <= 5){
        cout << ii << ". Hello World" << endl;
        ii++;
    }
    
    
    
    // array
    double angka_[3] = {100.0, 200.4, 300.7};

    cout << "Hasil indeks pertama : " << angka_[0] << endl;
    cout << "Hasil aray : " << angka_ << endl;
    
    
    //array 2 dimensional
    double angka[2][3] = {
        {100.0, 200.4, 300.7},
        {400.0, 500.5, 600.6}
    };

    cout << "Hasil indeks pertama : " << angka[0][0] << endl;
    cout << "Hasil indeks kedua : " << angka[1][2] << endl;

    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 3; j++){
            cout << angka[i][j] << " ,";
        }
        cout << endl;
    }
    

    
    //array 3 dimensional
    double angka1[2][3][2] = {
        {
            {100.0, 200.4},
            {300.7, 400.8},
            {500.9, 600.1}
        },
        {
            {700.2, 800.3},
            {900.4, 1000.5},
            {1100.6, 1200.7}
        }
    };
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 3; j++){
            for(int k = 0; k < 2; k++){
                cout << angka1[i][j][k] << " ,";
            }
            cout << endl;
        }
        cout << endl;
    }
    
    
   
    // sizeof
    double angka22[3] = {100.0, 200.4, 300.7};
    for(int i = 0; i < sizeof(angka22)/sizeof(angka22[0]);i++){
        cout << angka22[i] << " ,";
    }
    
    // mengganti elemen array  
    double angka11[3] = {100.0, 200.4, 300.7};
    
    angka11[1] = -100.0;
    for(int i = 0; i < sizeof(angka11)/sizeof(angka11[0]);i++){
        cout << angka11[i] << " ,";
    }
    
    
    int n[2][3] = {
        {1,2,3},
        {4,5,6}
    };

    // tipe data string
    string greeting = "Selamat Pagi";
    cout << greeting;

    // memisahkan string
    char greets[] = "Selamat Pagi";
    int len = sizeof(greets) / sizeof(greets[0])-1;

    for(int i = 0; i < len; i++){
        if(len == i+1){
            cout << greets[i];
        } else {
            cout << greets[i] << ", ";
        }
    }
    #endif
    
}
