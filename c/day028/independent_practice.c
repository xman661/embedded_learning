#include <stdio.h>
#include <stdlib.h>

int main(void) {
    system("chcp 65001 > nul");
    int x = 5, y = 99;
    int *px = &x;
    int *py = &y;
    printf(" px = %p  *px = %d\n py = %p  *py = %d\n", px, *px, py, *py);
    int temp = *px;
    printf(" px = %p  *px = %d\n py = %p  *py = %d\n", px, *px, py, *py);
    *px = *py;
    printf(" px = %p  *px = %d\n py = %p  *py = %d\n", px, *px, py, *py);
    *py = temp;
    printf(" px = %p  *px = %d\n py = %p  *py = %d\n", px, *px, py, *py);
    return 0;
}