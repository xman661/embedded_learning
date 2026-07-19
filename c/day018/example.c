#include <stdio.h>
#include <stdlib.h>

int add(int a, int b);
int subtract(int a, int b);
int larger(int a, int b);

int main(void) {
    system("chcp 65001 > nul");
    int x = -3;
    int y = -8;

    int sum = add(x,y);
    int max = larger(x,y);
    int result = subtract(x,y);
    printf("加法结果: %d, 最大值: %d, 减法结果: %d\n", sum, max, result);
    return 0;

}

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int larger(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
} 