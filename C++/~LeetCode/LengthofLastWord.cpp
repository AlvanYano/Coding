#include <iostream>
#include <string.h>

using namespace std;

class Solution {
    public:
        int lengthOfLastWord(string s) {

            int start, end = -1;
            string last_word, get_word;

            do {
                start = end + 1;
                
                end = s.find("", start);

                get_word = s.substr(start, end - start);
            
                if (get_word != ""){
                    last_word = get_word;
                }

            } while (end != -1);
            
            

            return last_word.size();

        }
    };

int main(){

    Solution coba;

    string input = "luffy is still joyboy";

    cout << coba.lengthOfLastWord(input) << endl;

}