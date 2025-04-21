#include <stdio.h>
#include <string.h>

int main(){
    char list1[] = "[({";
    char list2[] = " (";

    int hasil = strcmp(list1, list2);

    printf("%d", hasil);

}