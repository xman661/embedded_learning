// while (条件) {
//    条件为真时重复执行
// }

#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001 > nul");
    int i = 10;
    while (i >= 1) {
        printf("%d ", i);
        i--;      
    }
    printf("\n");

    for (i = 10; i >= 1;i--) {
        printf("%d ",i);
    }
    printf("\n");

    i = 10;
    do {
        printf("%d ", i);
        i--;
    } while (i >= 1);
    printf("\n");
    
    i = 2;
    int sum = 0;
    while (i <= 100) {
        sum = sum + i;
        i+=2;
    }
    printf("2到100的偶数和为：%d\n", sum);

    return 0;
}

