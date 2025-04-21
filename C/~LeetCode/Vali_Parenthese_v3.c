#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool isMatch(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '[' && close == ']') ||
           (open == '{' && close == '}');
}

bool isValid(char* s) {
    int len = strlen(s);
    char* stack = (char*)malloc(len);
    int top = 0;

    for (int i = 0; i < len; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            stack[top++] = c;
        } else {
            if (top == 0) {
                free(stack);
                return false;
            }
            if (!isMatch(stack[top - 1], c)) {
                free(stack);
                return false;
            }
            top--; // pop
        }
    }

    bool valid = (top == 0);
    free(stack);
    return valid;
}

int main() {
    char s[] = "([{}])";
    printf("%s\n", isValid(s) ? "Valid" : "Invalid");
    return 0;
}
