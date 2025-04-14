#include <stdio.h>
#include <string.h>

int *return_coba;

int input_func = 10;

char *var_coba[20][10] = {"kikan", "ikan", "ma"};
// char *var_coba_poin = var_coba;
char **var_coba_poin_1 = var_coba;

int var_arr[5] = {1,2,3,4};

void cobaFunction(int **coba){

    // printf("%p \n", coba);
    // printf("%p \n", *coba);
    // printf("%p \n", var_coba_poin);

    printf("%s \n", coba[0][1]);

    // return *coba;

}


int pointer_to_char;
/*
char* longestCommonPrefix(char** strs, int strsSize) {

    for(int i = 0; i < sizeof(*strs)/sizeof(char); i++){
        
        for (size_t j = 0; j < strlen(*strs[i]); j++){
            pointer_to_char = *strs[i];
            
        }
        

    }

}
    */

int main(){

    // printf("%p \n", var_coba_poin);
    // printf("%p \n", var_coba_poin);
    // printf("%p \n", var_coba_poin_1);

    // printf("%d \n", *var_coba_poin_1);


    // input_func = 10;

    // return_coba = cobaFunction(var_coba_poin_1);

    // printf("%p \n", return_coba);
    // printf("%d", *return_coba);

    // for (int i = 0; i < 10; i++){

    //     printf("%d \n", i);
    // printf("%s %s %s\n", var_coba[0], var_coba[1], var_coba[2]);
    // printf("%s \n", *var_coba_poin_1[0]);

    cobaFunction(*var_coba_poin_1);
        
    
    // }

}