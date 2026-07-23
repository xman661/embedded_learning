#include <stdio.h>
#include <stdlib.h>



int main(void) {
    system("chcp 65001 > nul");
    int a = 10;
    printf("%d, %p", a, &a);
    printf("\n");
    int *p = &a;
    printf("p = %p, *p = %d\n ",p, *p);
    *p = 20;
    printf("a = %d, *p = %d\n", a, *p);
    return 0;
}