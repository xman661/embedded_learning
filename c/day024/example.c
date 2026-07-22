#include <stdio.h>
#include <stdlib.h>

void print_array(int arr[], int size) {
    for(int i =  0; i < size; i++) {
        printf("[%d] ", arr[i]);
    }
    printf("\n");
}

int sum_array(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}
 
int max_array(int arr[], int size) {
    int max = arr[0];
    for(int i = 1; i < size; i++) {
        if(arr[i] > max) {
            max = arr[i];
        } 
    }
    return max;
}

double average_array(int arr[], int size) {
    int sum = sum_array(arr, size);
    return (double)sum / size;
}

int main(void) {
    system("chcp 65001 > nul");
    int scores[] = {10, 20, 30, 40, 50};
    int size = 5; 
    print_array(scores, size);
    printf("总和：%d\n", sum_array(scores, size));
    printf("最大值：%d\n", max_array(scores, size));
    printf("平均值：%.2f\n", average_array(scores, size));
    return 0;
}