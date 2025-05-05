#include <iostream>

using namespace std;

int main(){
 
    int golongan_179;

    cout << "Masukan Golongan : ";

    cin >> golongan_179;

    switch (golongan_179) {
        case 1:
            cout << "Golongan 1" << endl;
            break;
        case 2:
            cout << "Golongan 2" << endl;
            break;
        case 3:
            cout << "Golongan 3" << endl;
            break;
        default:
            cout << "Golongan tidak valid" << endl;
    }

}