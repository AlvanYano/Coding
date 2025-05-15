#include <iostream>
#include <vector>

using namespace std;

int main(){
    
    vector<string> coba = {"1" , "2", "3"};

    string gabung = coba[0] + coba[1] + coba[2];

    cout << gabung << endl;

    int baru = stoi(gabung);

    string baru_1 = to_string(baru);

    cout << baru + 5 << endl;

    

}