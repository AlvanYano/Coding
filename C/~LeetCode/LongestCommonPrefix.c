#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    int minLength = strlen(strs[0]);
    
    // Find the minimum string length
    for (int i = 1; i < strsSize; i++) {
        int len = strlen(strs[i]);
        if (len < minLength) {
            minLength = len;
        }
    }

    char* prefix = (char*)malloc(sizeof(char) * (minLength + 1));
    int i;

    for (i = 0; i < minLength; i++) {
        char ch = strs[0][i];
        printf("%c \n", ch);
        printf("%d \n", i);
        printf("%d", minLength);

        for (int j = 1; j < strsSize; j++) {
            if (strs[j][i] != ch) {
                prefix[i] = '\0';
                return prefix;
            }
        }

        prefix[i] = ch;
    }

    prefix[i] = '\0';
    return prefix;
}

int main(){
    char* input[] = {"flower", "flow", "flight"};
    int jumlah = 3;
    char* hasil = longestCommonPrefix(input, jumlah);
}