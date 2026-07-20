#include  <stdio.h>
#include <stdlib.h>

int main() {
    system("chcp 65001 > nul");
    int Product_output[6] = {100, 200, 150, 50, 250, 300};
    int i;
    int max = Product_output[0];
    int min = Product_output[0];
    int sum = 0;
    for(i = 0; i < 6; i++) {
        if(Product_output[i] > max) {
            max = Product_output[i];
        }
        if(Product_output[i] < min) {
            min = Product_output[i];
        }
        sum += Product_output[i];
    }
    double average = (double)sum / 6;
    printf("最大值：%d,最小值：%d,平均值：%.2f\n", max, min, average);
    return 0;
}