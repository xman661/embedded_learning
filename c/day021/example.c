#include <stdio.h>
#include <stdlib.h>



int main(void) {
    system("chcp 65001 > nul");
    int i;
    int sum = 0;
    int scores[5] = {85, 90, 78, 92, 88};
    int max = scores[0];
    int min = scores[0];
    for(i = 0; i < 5; i++){
        if(scores[i] > max) {
            max = scores[i];
        }
        if(scores[i] < min) {
            min = scores[i];
        }
        sum += scores[i];
    }
    double average = (double)sum / 5;
    printf("max = %d, min = %d,sum = %d, average = %.2f\n", max, min, sum, average);
    return 0;
}