#include <stdio.h>
#include <stdlib.h>

int main() {
    system("chcp 65001 > nul");
    int sum = 0;
    int number;
    int i = 0;
    int positive_count = 0;
    do {
        scanf("%d", &number);
        printf("当前输入的数是：%d\n", number);
        if (number > 0) {
            positive_count++;
        }
        sum += number;
        i++;
    } while (i < 5);
    printf("五个整数的和是：%d,正数数量:%d\n", sum, positive_count);
    return 0;
}