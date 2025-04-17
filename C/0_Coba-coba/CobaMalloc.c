#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** cobaMal(int* panjang, char* string){

    char** dua_dimensi_arr = (char**)malloc(*panjang * sizeof(char*)); 
    // array ini akan berisi *char

    for (int i=0;i<*panjang;i++){
        dua_dimensi_arr[i] = (char*)malloc(strlen(string) * sizeof(char));
        // aray ini akan berisi char, jadi satu tingkat di bawahnya 
        // semisal jenis variabelnya adalah char* maka isinya adalah char
        // jika char** maka isinya akan char*
        // jika char*** maka isinya akan char**
        
    }

    for (int i = 0; i <*panjang; i++){
        strcpy(dua_dimensi_arr[i], string);

    }
    
    return dua_dimensi_arr;

}

int main(){

    // char** valMall = (char**)malloc(sizeof(char*)*10);

    // valMall[1] = "ikan";
    // valMall[0] = "saya";

    // printf("%s", valMall[0]);

    int panjang = 10;
    char** return_mall;
    char str[] = "Saya Ikan \n";


    return_mall = cobaMal(&panjang, str);

    for (int i = 0; i<panjang;i++){
        printf("%s",return_mall[i]);

    }

    for (int i = 0; i<panjang; i++){
        free(return_mall[i]);

    }
    free(return_mall);



}