#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int len_str_now;
int len_str_shortest = 201, idx_shortest, result_length;
char dyna_char[200] = "";

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        return "";
    }

    // printf("%d", strsSize);

    int i;

    for (i = 0; i<strsSize; i++){
        len_str_now = strlen(strs[i]);
        if (len_str_now < len_str_shortest){
            len_str_shortest = len_str_now;
            idx_shortest = i;
        }
    }

    char* prefix = strs[idx_shortest];
   
    // printf("%d", idx_shortest);

    for (int i = 0; i < strlen(prefix); i++){

        char get_first = prefix[i]; 

        // printf("%c\n", get_first);

        for(int j = 0; j < strsSize; j++){

            char* prefix_comp = strs[j];

            if (prefix_comp[i] != get_first){
                return dyna_char;

            }

            if (strsSize-1 == j){
                dyna_char[result_length++] = get_first;
                // printf("%s\n", dyna_char);
                
            
            }
        }
    }
}

int main() {
    char* input[] = {"flwer", "flow", "flight"};
    
    char* result = longestCommonPrefix(input, 3);

    printf("%s", result);

    // free()
    
}

