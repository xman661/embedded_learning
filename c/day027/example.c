#include <stdio.h>
#include <stdlib.h>

int matrix[4][4];

int main(void) {
    system("chcp 65001 > nul");  
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            matrix[i][j] = i * j;
            printf("%d ", matrix[i][j]);
        }
         printf("\n");
    }
    return 0;
}