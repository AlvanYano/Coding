#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

class Solution {
    public:
        int searchInsert(vector<int>& nums, int target) {
            for(int i = 0; i < nums.size(); i++){
                if (nums[i] == target){
                    return i;

                } else {
                    if (nums[i] > target){
                        return i;
                    }
                }
            }
            return nums.size();
        }
    };

int main(){

    vector<int> coba = {1,3,5,6};
    int target = 4;
    
    Solution cobam;

    int hasil = cobam.searchInsert(coba, target);

    cout << hasil << endl;
    
    

}
