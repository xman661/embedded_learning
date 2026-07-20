#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    system("chcp 65001 > nul");
    char full_name[10];
    strcpy(full_name, "Zhang");
    strcat(full_name, " ");
    strcat(full_name, "San");
    printf("'full_name' : %s\n",full_name);
    printf("'full_name'的长度：%zu\n",strlen(full_name));
    if(strcmp(full_name, "Zhang San") == 0) {
        printf("姓名相同\n");
    } else {
        printf("姓名不相同\n");
    }
    return 0;
}