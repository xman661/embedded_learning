#include <stdio.h>
#include <stdlib.h>

int main(void) {
    system("chcp 65001 > nul");
    char word[] = "embedded";
    int count = 0;
    for(int i = 0; word[i] != '\0'; i++) {
        printf("逐个字符检查: %c\t", word[i]);
        if(word[i] == 'e') {
            count++;
        }
    }
    printf("'e' 出现: %d 次 \n", count);
    return 0;
}