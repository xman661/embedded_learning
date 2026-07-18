#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001 > nul");
    int sum = 0;
    for(int i = 1; i <= 100; i++) {
        sum += i;
    }
    printf("1到100的和为：%d\n", sum);
    return 0;
}