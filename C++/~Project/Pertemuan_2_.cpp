#include <iostream>

using namespace std;

int main(){

    // #ifdef on
    
    cout << "Teknik Elektro Undip" << endl;
    cout << "nama : Alvan Fabiyano" << endl;
    
    // membuat rumus luas lingkaran l = phi * r * r
    float phi= 3.14;
    float l;
    float r;

    // menginput r
    cout << "masukan jari jari lingkaran = ";
    cin >> r;

    // hitung nilai luas 
    l = phi * r * r;
    
    // menampilkan l
    cout << "luas lingkaran = " << l << endl;

    cout << "Menghitung Volume Bola" << endl;

    // input jari jari bola
    cout << "Berapa jari - jari bolanya : ";
    cin >> r;

    // hitung volume bola
    float v;
    v =  phi * r * r * r * 4/3;

    cout << "Luasnya adalah " << v << endl;

    int a, b, c, d;

    cout << "Input a ";
    cin >> a;
    cout << "Input b ";
    cin >> b;
    cout << "Input c ";
    cin >> c;

    // menghitung rumus d = a * b + b * c + 2 * a * c;

    d = a * b + b * c + 2 * a * c;

    cout << "Hasil Perkalian = " << d << endl;

    // percabangan : looping and conditional

    // PERCABANGAN / kondisional

    // menentukan sebuah angka genap atau ganjil

    

    int angka;
    cout << "Masukan sebuah angka = ";

    cin >> angka;

    if (angka % 2 == 0){
        cout << "Angka Genap" << endl;

    } else {
        cout << "Angka Ganjil" << endl;

    }


    // operator pembanding  < , > < <= , >= , != , ==
    // mengkonversi nilai k ebobot 
    // A-> 4 B -> 3 C-> 2 D-> 1 E-> 0

    // menginputkan nilai
    char nilaimu;
    cout << "Masukan nilai (A/B/C/D/E) = ";
    cin >> nilaimu;

    int bobot;

    if (nilaimu == 'A'){
    bobot = 4;
    } else if (nilaimu == 'B'){
        bobot = 3;
    } else if (nilaimu == 'C'){
        bobot = 2;
    } else if (nilaimu == 'D'){
        bobot = 1;
    } else if (nilaimu == 'E'){
        bobot = 0;
    } else {
        cout << "Anda memasukan huruf yang salah" << endl;
    }

    cout << "Bobotnya adalah " << bobot << endl;

    


    string gaji;
    int golongan;

    cout << "Golongan Anda : ";
    cin >> golongan ;

    if (golongan == 1){
        gaji = "1000000";
    } else if (golongan == 2){
        gaji = "2000000";
    } else if (golongan == 3) {
        gaji = "3000000";
    } else if (golongan == 4){
        gaji = "4000000";
    } else if (golongan == 5){
        gaji = "5000000";
    }

    cout << "Gaji anda : " << gaji << endl;

    int nilai;
    char hasil;

    cout << "Masukan nilai kamu : ";
    cin >> nilai;

    if (nilai >= 80){
        hasil = 'A';
    } else if (nilai < 80 and nilai >= 70){
        hasil = 'B';
    } else if (nilai < 70 and nilai >= 60){
        hasil = 'C';
    } else if (nilai < 60 and nilai >= 50){
        hasil = 'D';
    } else if (nilai < 50){
        hasil = 'E';
    }
    
    cout << "Kamu dapat skor " << hasil << endl;

    
    string username_simpan = "mahasiswa1";
    int pass_simpan = 12345;

    string username;
    int password;


    cout << "masukan usernam : ";
    cin >> username;

    cout << "masukan pass : ";
    cin >> password;

    if (username == username_simpan){
        if (password == pass_simpan){
            cout << "Username dan Password benar"<< endl;
        }
    } else{
        cout << "Sandi atau password salah"<< endl;
    }

    // perulangan / looping

    for (int i = 0;i<100;i++){
        
        cout << "Teknik Elektro " << i <<endl;
    
    }

    
    // #endif

    int n = 7;
    int faktorial = 1;
    for (int i = 1; i <= n; i++){
        faktorial = i * faktorial;

    }


    cout << "Faktorial : "<<faktorial << endl;



}


