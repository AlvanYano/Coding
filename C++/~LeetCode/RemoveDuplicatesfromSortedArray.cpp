// ini benar tapi tidak bisa di compile di LeetCode jadi saya akan buat baru 
// dengan logika yang lebih simple dari chatgpt

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            if (nums.size() == 0) return 0;

            int len_nums = nums.size();
            int past = 0;

            for (int i = 1; i < len_nums; i++){

                while (nums[i] == nums[past]){                
                    if ((nums.begin() + i) == nums.end()){
                        return nums.size();
                    }

                    nums.erase(nums.begin() + i);
                }
                past++;
            }
        }
    };


int main() {

    Solution coba;

    vector<int> arr = {1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5};

    int hasil = coba.removeDuplicates(arr);

    cout << hasil << endl;

}