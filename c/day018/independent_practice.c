#include <stdio.h>
#include <stdlib.h>

int square(int n);

int main(void) {
    system("chcp 65001 > nul");
    printf("square(3) = %d\n", square(3));
    printf("square(0) = %d\n", square(0));
    printf("square(-4) = %d\n", square(-4));
    return 0; 
}

int square(int n) {
    return n * n;
} 