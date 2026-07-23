#include <stdio.h>
#include <stdlib.h>

int matrix[3][3];

int main(void) {
    system("chcp 65001 > nul");
    int sum = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    for(int i = 0; i < 3; i++) {
        sum += matrix[i][i];
    }
    printf("主对角线元素之和：%d\n", sum);
    return 0;
}