#include <stdio.h>
#include <stdlib.h>

int main(void) {
    system("chcp 65001 > nul");
    int i = 0;
    char name[] = "Alice";
    char word[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    printf("打印： %s, %s\n", name, word);
    while(name[i] != '\0') {
        printf("逐个打印为：%c\t", name[i]);
        i++;
    }
    printf("\n");
    for(i = 0; name[i] != '\0'; i++) {
        printf("逐个打印为：%c\t", name[i]);
    }
    printf("\nname[0] = %c\n", name[0]);
    return 0;
}
