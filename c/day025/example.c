#include <stdio.h>
#include <stdlib.h>

void print_scores(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        printf("%d\n", arr[i]);
    }
}

int sum_scores(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
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

int count_pass(int arr[], int size) {
    int counts = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] >= 60) {
            counts++;
        }
    }
    return counts;
}

void show_menu(void) {
    printf("====== 成绩统计菜单 ======\n 1. 查看成绩\n 2. 查看总分和平均分\n 3. 查看最高分和最低分\n 4.查看及格人数\n 0. 退出\n 请选择：");
}

int main(void) {
    system("chcp 65001 > nul");
    int choice;
    int scores[5] = {86, 59, 75, 48, 60};
    int size = 5;


    do {
        show_menu();
        scanf("%d", &choice);
        if(choice == 1) {
            print_scores(scores, size);
        } else if (choice == 2) {
            printf("总分为：%d\n", sum_scores(scores, size));
        } else if (choice == 3) {
            printf("最高分为：%d\n最低分为：%d\n", max_scores(scores, size), min_scores(scores, size));
        } else if(choice == 4) {
            printf("不及格数目：%d\n",count_pass(scores,size));
        } else if (choice == 0) {
            printf("再见！\n");
        } else {
            printf("无效选项\n");
        }
    } while (choice != 0);
    return 0;
}