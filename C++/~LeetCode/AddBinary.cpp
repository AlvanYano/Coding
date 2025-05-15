#include <iostream>
// #include <string>

#define BIGGER (a_len > b_len) ? a_len:b_len
#define IDX             \
if (BIGGER != a_len){   \
    b_len - a_len       \
} else {                \
    a_len - b_len       \
}                       \



using namespace std;

class Solution {
    public:
        string addBinary(string a, string b) {
            string sum;
            int carry = 0;
            int a_len = a.length();
            int b_len = b.length();
            int a1, b1, idx_1, idx_2;

            if (BIGGER =! a_len){   
                idx_2 = b_len - a_len; 
                cout << "TES" << endl;      
            } else {                
                idx_1 = a_len - b_len;      
            }                       
            
            // cout << a_len << endl;
            // cout << b_len << endl;

            for (int i = (BIGGER)-1; i >= 0; i--){

                if (BIGGER == a_len){

                    a1 = (a[i] == '1') ? 1 : 0;
                    // b1 = (b[i - idx_1] == '1') ? 1 : 0;

                    int coba = BIGGER;
                    cout <<  coba << endl;
                    int j = idx_1;
                    cout <<  j << endl;

                } else {
                    a1 = (a[i - idx_2] == '1') ? 1 : 0;
                    b1 = (b[i] == '1') ? 1 : 0;

                }

                // cout << carry << endl;
                // cout << a1 << endl;
                // cout << b1 << endl;
                                
                carry = a1 + b1 + carry; 

                if (carry >=2 ){
                    carry = 1;
                    sum = "0" + sum;
                
                } else if (carry == 1){
                    carry = 0;
                    sum = "1" + sum;
                
                } else{
                    carry = 0;
                    sum = "0" + sum;
                }

            }
            
            sum = ((carry == 1) ? "1" : "0" ) + sum;

            return sum;

        }
    };

int main(){

    // string coba = "SAYA";

    // for (int i = 0; i < 10;i++){
        
    //     // coba  = to_string(i) + coba;

    //     int u = coba[-1] == '\0';
    //     cout << u << endl;

    // }

    // cout << coba << endl;

    string a = "1010";
    string b = "1011";

    Solution coba;

    string hasil  = coba.addBinary(a, b);

    cout << hasil << endl;

}