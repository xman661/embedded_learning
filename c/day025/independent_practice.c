#include <stdio.h>
#include <stdlib.h>

void print_scores(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        printf("%d\n",arr[i]);
    }
}

int sum_scores(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

double average_scores(int arr[], int size) {
    int sum = sum_scores(arr, size);
    return (double)sum / size;
}

int max_scores(int arr[], int size) {
    int max = arr[0];
    for(int i = 1; i < size; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int min_scores(int arr[], int size) {
    int min = arr[0];
    for(int i = 1; i < size; i++) {
        if(arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

int count_scores(int arr[], int size) {
    int counts = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] < 60) {
            counts++;
        }
    }
    return counts;
}

void show_scores(void) {
    printf("===== 课程成绩统计 =====\n 1. 查看所有课程成绩\n 2. 查看总分和平均分\n 3. 查看最高分和最低分\n 4. 查看不及格课程数\n 0. 退出\n 请选择：");
}

int main(void) {
    system("chcp 65001 > nul");
    int choice;
    int scores[4] = {59, 83, 98, 29};
    int size = 4;

    do {
        show_scores();
        scanf("%d", &choice);
            if(choice == 1) {
                print_scores(scores, size);
            } else if(choice == 2) {
                printf("总分：%d\n平均分：%.2f\n", sum_scores(scores, size), average_scores(scores, size));
            } else if(choice == 3) {
                printf("最高分：%d\n最低分：%d\n", max_scores(scores, size), min_scores(scores, size));
            } else if(choice == 4) {
                printf("不及格数目：%d\n", count_scores(scores, size));
            } else if(choice == 0) {
                printf("再见！\n");
            } else {
                printf("输入无效\n");
            }
        } while(choice != 0);
        return 0;
    }