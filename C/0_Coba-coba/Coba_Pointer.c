#include <stdio.h>

void coba_function(char* val);

char var_array[10] = "AK";

int s1, s2, panjang_arr;

int main(){

    coba_function(var_array);

}

void coba_function(char* val){

    int *s1, *s2;

    s1 = val[0]; 
    s2 = val;

    panjang_arr = sizeof(val);

    printf("%c %s %s %d \n", s1, s2, val, panjang_arr);
    // printf("%p %p %p", *s1, *s2, *val);

}