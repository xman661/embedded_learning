#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    system("chcp 65001 > nul");
    char first[20] = "Hello";
    char second[] = "World";
    char copy[20];
    printf("'first'的长度：%zu\n",strlen(first));
    strcpy(copy, first);
    printf("copy : %s\n",copy);
    strcat(first, " ");
    strcat(first, second);
    printf("'first' : %s\n",first);
    if(strcmp(copy, "Hello") == 0) {
        printf("字符串相同\n");
    } else {
        printf("字符串不相同\n");
    }
    return 0;
}