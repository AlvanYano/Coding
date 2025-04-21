#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char open_paranthese[] = "([{";
char close_paranthese[] = ")]}";
int open_prt_Idx = 0;
int close_prt_Idx = 0;

bool isValid(char* s) {
    static int idx_plus;

    char* new_s = s + idx_plus++;

    //Function ngebedain open/close parentheses

    // //Ngetahuin panjang
    // int length_open = sizeof(open_paranthese) / sizeof(open_paranthese[0]);
    // int length_close = sizeof(close_paranthese) / sizeof(close_paranthese[0]);

    // //Jika panjang tidak sama, return false
    // if(length_open != length_close){
    //     return false;
    // }

    for(open_prt_Idx = 0;open_prt_Idx <= 3;open_prt_Idx++){
        if (open_paranthese[open_prt_Idx++] == new_s[0]){
            break;
        }
    }

    //Benerin nama variablenya, bisa dideklarasiin juga diFor (Best practices)
    for(open_prt_Idx = 0;open_prt_Idx <= 3;open_prt_Idx++){
        if (close_paranthese[close_prt_Idx++] == new_s[0]){
            break;
        }
    }

    if ((open_prt_Idx || close_prt_Idx) == 3){
        return false;
    } 
    if (open_prt_Idx != 3){
        
    }
    if (close_prt_Idx != 3){

    }


    

}

int main(){


}