#include <stdio.h>
#include <stdlib.h>

int sum_to_n(int n);

int main(void) {
    system("chcp 65001 > nul");
    printf("sum_to_n(10) = %d\n", sum_to_n(10));
    return 0;
}

int sum_to_n(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}