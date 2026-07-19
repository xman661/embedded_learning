#include <stdio.h>
#include <stdlib.h>

int sum_even_to_n(int n);
int larger(int a, int b);

int main(void) {
    system("chcp 65001 > nul");
    printf("sum_even_to_n(10) = %d\n", sum_even_to_n(10));
    printf("sum_even_to_n(100) = %d\n", sum_even_to_n(100));
    printf("larger(5, 10) = %d\n", larger(5, 10));
    printf("larger(10, 5) = %d\n", larger(10, 5));
    return 0;
}

int sum_even_to_n(int n) {
    int i;
    int sum = 0;
    for (i = 1; i <= n; i++){
        if (i % 2 == 0){
            sum += i;
        }
    }
    return sum;
}

int larger(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}