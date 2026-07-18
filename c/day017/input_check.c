#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001 > nul");
    int a;
    do {
        printf("请输入60到100之间的整数：");
        scanf("%d", &a);
        if (a < 60 || a > 100) {
            printf("输入超出范围，请重试 \n");
        }
    } while (a < 60 || a > 100);
    printf("您输入的整数是：%d\n", a);
    return 0;
}
