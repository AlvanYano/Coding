#include <stdio.h>
#include <string.h>
/*
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/

void cobaFunction(char * input);

int idx_in;

int char_val_now , char_val_future;
int output;

char var_char[20] = "MMMMMMDDDDDDDVIII";

int Char_To_Val(char * value){
    switch (*value)
    {
    case 'I':
        return 1;
    case 'V':
        return 5;
    case 'X':
        return 10;
    case 'L':
        return 50;
    case 'C':
        return 100;
    case 'D':
        return 500;
    case 'M':
        return 1000;
    default:
        return 0;
    } 
}
int romanToInt(char *s) {
    
    int panjang_s = strlen(s);
    s[panjang_s] = '\n';

    char_val_now = Char_To_Val(&s[idx_in++]);


    while (1)
    {
        char_val_future = Char_To_Val(&s[idx_in++]);

        if (char_val_future > char_val_now){
            output -= char_val_now;

        } else {
            output += char_val_now;

        }

        char_val_now = char_val_future;

        if (char_val_now == 0){
            break;
        }

    }    

    return output;

}

int main(){

    printf("%d",romanToInt(var_char));



    // cobaFunction(var_char);

}


void cobaFunction(char * input){

    if (!input[100]){
        
        printf("acc");

    }

}