#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

int main() {
    struct ListNode* head = NULL;
    struct ListNode* temp;
    struct ListNode* newNode;

    // Tambahkan 3 node
    for (int i = 1; i <= 6; i++) {
        newNode = malloc(sizeof(struct ListNode));
        newNode->val = i;
        newNode->next = NULL;

        if (head == NULL) { 
            head = newNode;  // node pertama
        } else {
            temp = head;
            while (temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    // Cetak isi linked list
    temp = head;
    printf("Linked list:\n");
    while (temp != NULL) {
        printf("%d -> ", temp->val);
        temp = temp->next;
    }
    printf("NULL\n");

    // Bebaskan memori
    temp = head;
    while (temp != NULL) {
        struct ListNode* toDelete = temp;
        temp = temp->next;
        free(toDelete);
    }

    return 0;
}
