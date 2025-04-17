#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char hasil;
// Fungsi menerima char** karena array of string = array of char pointer
char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    // Contoh: mengakses karakter ke-2 dari string pertama
    char get_val = strs[0][1];  // misalnya ambil 'l' dari "flower"
    // printf("Karakter kedua dari string pertama: %c\n", get_val);

    // Kembalikan pointer ke karakter yang valid

    hasil = strs[0][0] | strs[0][0];

    return &hasil;
}

int main() {
    char* input[] = {"flower", "flow", "flight"};
    int jumlah = 3;

    char* hasil = longestCommonPrefix(input, jumlah);

    // Tampilkan hasil akses karakter
    printf("Karakter yang dikembalikan dari fungsi: %c\n", *hasil);

    return 0;
}
