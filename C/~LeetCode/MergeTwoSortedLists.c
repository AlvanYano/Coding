#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode *next;
};



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    
    struct ListNode* cek_null = list1; 
    int idx_get = 0;

    int* get_val = (int *)malloc(sizeof(int));
    struct ListNode** get_node = (struct ListNode**)malloc(sizeof(struct ListNode*));

    while(cek_null->next != NULL){
        get_val[idx_get] = cek_null->val;
        get_node[idx_get++] = cek_null;

        get_val = realloc(get_val,sizeof(int) * idx_get);
        get_node = realloc(get_node,sizeof(struct ListNode*) * idx_get);

        cek_null = cek_null->next;
    }

    struct ListNode* cek_null = list2; 

    while(cek_null->next != NULL){
        get_val[idx_get] = cek_null->val;
        get_node[idx_get++] = cek_null;

        get_val = realloc(get_val,sizeof(int) * idx_get);
        get_node = realloc(get_node,sizeof(struct ListNode*) * idx_get);

        cek_null = cek_null->next;
    }

    int i, j, temp_val;
    
    struct ListNode* temp_node;

    for(i = 0; i < idx_get-1; i++) {
        // Loop ke-n akan menempatkan elemen terbesar di posisi akhir
        for(j = 0; j < idx_get-i-1; j++) {
            if(get_val[j] > get_val[j+1]) {
                // Tukar elemen jika urutannya salah
                temp_val = get_val[j];
                get_val[j] = get_val[j+1];
                get_val[j+1] = temp_val;
                
                temp_node = get_node[j];
                get_node[j] = get_node[j+1];
                get_node[j+1] = temp_node;
            }
        }
    }

    struct ListNode* result = get_node[0];
    // untuk mengakhiri linked list
    get_node[idx_get] = NULL;

    for (int i = 1;i<idx_get+1;i++){
        result->val = get_val[i-1];
        result->next = get_node[i];
    }

    free(get_node);
    free(get_val);

    return result;
}

int main(){

    
    
}