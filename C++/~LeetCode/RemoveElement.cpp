#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            
            int len_nums = nums.size();
            
            for(int i = 0; i < len_nums; i++){
                if (nums[i] == val){
                    vector<int>::iterator hasil = find(nums.begin(), nums.end(), val);
                    nums.erase(hasil);
                    i--;
                    len_nums--;
                }

                cout << len_nums << endl;
                cout << nums[i] << endl;

            }
            
            return nums.size();
        }
    };

int main(){


    vector<int> arr = {3, 2, 2,3};

    // vector<int>::iterator hasil = find(arr.begin(), arr.end(), 11);

    // cout << *hasil<< endl;

    // arr.erase(hasil);

    for (int i : arr){
        
        if (i == 1){
            vector<int>::iterator hasil = find(arr.begin(), arr.end(), i);
            arr.erase(hasil);
        }

    }
    
    Solution coba;

    int hasil = coba.removeElement(arr, 3);

    cout << hasil << endl;
    // for (int i : arr){
    //     cout << i << " ";
    // }

}
