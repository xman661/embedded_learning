#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001 > nul");
    printf("Hello, World!\n");

    // F = C * 9/5 + 32
    float celsius = 25.0;
    float fahrenheit = celsius * 9.0 / 5.0 + 32.0;
    printf("%.2f = %.2f\n", celsius, fahrenheit);

    // 判断温度的高低
    if (celsius > 30) {
        printf("好热啊\n");
    } else if (celsius > 20){
        printf("好温暖啊\n");
    } else {
        printf("好冷啊\n");
    }

    return 0;
}