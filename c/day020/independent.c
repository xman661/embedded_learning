#include <stdio.h>
#include <stdlib.h>

int main() {
    int i;
    int times[7] = {45, 30, 60, 50, 40, 55, 35};
    for(i = 0; i< 7; i++) {
        printf("第%d天学习时间为：%d分钟\n", i + 1, times[i]);
    }
    return 0;
}