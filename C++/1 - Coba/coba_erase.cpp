#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates(vector<int>& nums) {
    int len_nums = nums.size();

    for (int i = 0; i < len_nums; i++){

        while (nums[i] == nums[i+1]){
            if (nums.begin() + 1 + i == nums.end()){
                return nums.size();
            }
            nums.erase(nums.begin() + i + 1);

        }
    }
}

int main(){

    vector<int> arr = {1, 1,1,1,1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5};

    // arr.erase(arr.begin());

    // cout << arr.size() << endl; 


    int j;

    // for (int i = 0 ; i < arr.size();i++){
        // arr.erase(arr.begin() + i);

        // cout << i << endl;

        // j++;
    // }

    // arr.erase(1);

    // cout << j << endl;

    int hasil = removeDuplicates(arr);

    cout << hasil << endl;

}