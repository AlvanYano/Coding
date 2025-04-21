#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

char open_paranthese[] = "([{";
char close_paranthese[] = ")]}";



int charToNumber(char var){
    switch (var) {
    case '{':
        return 10;
    case '[':
        return 20;
    case '(':
        return 30;
    case '}':
        return 10;
    case ']':
        return 20;
    case ')':
        return 30;
    }
}


bool isValid(char* s) {

    int* temp_list = (int *)malloc(sizeof(int));
    int temp_ptr_length = 0;
    int ptr_idx = 0;
    
    for (int i = 0; i<strlen(s);i++){
        for (ptr_idx; ptr_idx < strlen(s); ptr_idx++){

            // printf("tr %d\n", strchr(open_paranthese, s[ptr_idx]) != NULL);
            // printf("ss %c\n", s[ptr_idx]);


            if (strchr(open_paranthese, s[ptr_idx]) != NULL){
                temp_list[temp_ptr_length] = charToNumber(s[ptr_idx]);
                // printf("tla %d\n", temp_ptr_length);
                temp_list = realloc(temp_list, ++temp_ptr_length * sizeof(int));
                printf("tla %d\n",temp_ptr_length);
            } else {
                break;
            }
            // printf("a %d\n", ptr_idx);
            
            // printf("aa %d \n", temp_ptr_length);
        }

        // printf("%d \n", temp_list[0]);
        // printf("%d \n", temp_list[1]);
        // printf("%d \n", temp_list[2]);
        // printf("%d \n", strlen(s));


        for (ptr_idx; ptr_idx < strlen(s); ptr_idx){

            printf("cb %d \n", temp_ptr_length);

            int coba = charToNumber(s[ptr_idx]);

            temp_ptr_length = temp_ptr_length - 1;
            int coba1 = temp_list[temp_ptr_length];
            ptr_idx++;
            
            printf("tlb %d \n", temp_ptr_length);
            printf("b %d\n", coba);
            printf("vb %d\n", coba1);
            if(coba1 != coba){
                return 0;
            
            }
            if (temp_ptr_length == 0){
                printf("cp\n");
                break;
            }
            // printf("s\n");
        }
    }
    free(temp_list);

    return 1;

}

int main(){

    // char s[] = "([])";
    // char s[] = "()[]{}";
    // char s[] = "(]";
    char s[] = "()";

    int retun = isValid(s);

    printf("%d",retun );

}