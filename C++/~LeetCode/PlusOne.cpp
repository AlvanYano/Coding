#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> plusOne(vector<int>& digits) {

            for (int i = digits.size() - 1; i >= 0; i--){

                if (digits[i] != 9){
                    digits[i]++;
                    return digits;
                
                } else {
                    if (i == 0){
                        digits[i] = 1;
                        digits.push_back(0);
                        return digits;

                    } else {
                        digits[i] = 0;

                    }

                } 

            }
            return digits;
        }
    };

int main(){

    Solution coba_m;

    vector<int> coba = {1, 9, 9,9};

    vector<int> hasil =coba_m.plusOne(coba);
    
    for (int i = 0; i < hasil.size(); i++){
        cout << hasil[i] << " ";
    }

    cout << endl;


}