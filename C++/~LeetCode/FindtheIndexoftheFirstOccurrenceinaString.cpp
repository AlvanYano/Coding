#include <iostream>
#include <string>

using namespace std;


class Solution {
    public:
        int strStr(string haystack, string needle) {

            for (int i = 0; i <= haystack.length();i++){
                
                int i2 = i;

                for(int j = 0; j < needle.length(); j++){

                    if (haystack[i2] != needle[j]){
                        break;
                    }
                    
                    if (j == needle.length()-1){
                        return i;
                    }
                    i2++;

                    if (i2 == haystack.length()){
                        return -1;
                    }
                }

                if (i == haystack.length()-1){
                    return -1;
                }
            }
            return -1;
        }
    };

int main(){
    Solution coba;

    int hasil = coba.strStr("abc", "c");

    cout << hasil << endl;
    

}