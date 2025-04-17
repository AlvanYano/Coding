#include <stdio.h>
#include <string.h>

// char* cobaMal(char)

char** awal[5]; 
// jadi ini tipe datanya adalah char**, jadi berisi pointer di masing masing
// indeks nya


char* idx_1[2];
char* idx_2[2];
char* idx_3[2];

// char idx_1[2] = "i1";
// char idx_2[2] = "i2";
// char idx_3[2] = "i3";

char idx_1_1[2] = "AB";
char idx_1_2[2] = "AU";

char idx_2_1[2] = "AI";
char idx_2_2[2] = "AC";

char idx_3_1[2] = "AO";
char idx_3_2[2] = "AP";

int main(){

    awal[0] = idx_1;
    awal[1] = idx_2;
    awal[2] = idx_3;


    idx_1[0] = idx_1_1;
    idx_1[1] = idx_1_2;

    idx_2[0] = idx_2_1;
    idx_2[1] = idx_2_2;
 
    idx_3[0] = idx_3_1;
    idx_3[1] = idx_3_2;

    printf("%s", awal[0][0]);

    // strcpy(**awal[1], "IO");

    printf("%c", **awal[1]);
    // printf("%d", sizeof(char**));

}