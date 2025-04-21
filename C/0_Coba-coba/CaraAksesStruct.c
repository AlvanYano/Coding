#include <stdio.h>

struct ListNode {
    int val;

    
};

void CobaAkses(struct ListNode* list1) {
    printf("%d", list1->val);

}


int main(){
    struct ListNode coba_struct;
    
    coba_struct.val = 10;

    CobaAkses(&coba_struct);
    
}