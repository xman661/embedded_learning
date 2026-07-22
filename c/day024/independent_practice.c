#include <stdio.h>
#include <stdlib.h>

void print_array(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        printf("[%d] ",arr[i]);
    }
    printf("\n");
}

int count_even(int arr[], int size) {
    int counts = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) {
            counts++;
        }
    }
    return counts;
}

int min_array(int arr[], int size) {
    int min = arr[0];
    for(int i = 1; i < size; i++) {
        if(arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

int main(void) {
    system("chcp 65001 > nul");

    int counts[6] = {13,-14,34,22,29,-29};
    int size = 6;
    print_array(counts,size);
    printf("偶数个数：%d\n", count_even(counts,size));
    printf("最小值：%d\n", min_array(counts,size));
    return 0;
}