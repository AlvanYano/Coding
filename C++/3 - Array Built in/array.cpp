#include <iostream>
#include <array>

using namespace std;

array <int, 5> arr_val;

int main(){

    cout << &arr_val << endl;

    for(int &var : arr_val){
        cout << &var << " " << var << endl;
    }

}
