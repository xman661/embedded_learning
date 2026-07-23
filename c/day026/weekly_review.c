#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// ========== 盲打检查 Day 22~25 ==========
// 你凭记忆在每题下方的区域写代码，写完告诉我，我帮你检查。

// -------------------- 题目 1 (Day 22) --------------------
// 声明 word[] = "embedded"，for 循环遍历打印每个字符
// -------------------- 题目 2 (Day 23) --------------------
// first[20] = "Zhang"; last[] = "San"; 拼成 "Zhang San"


// -------------------- 题目 3 (Day 24) --------------------
// count_even(arr, size) 统计偶数个数
int count_even(int arr[], int size) {
    int counts = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) {
            counts++;
        }
    }
    return counts;
}

// -------------------- 题目 4 (Day 25) --------------------
// do-while 菜单循环：显示菜单、读选项、0退出
void show_menu(void) {
    printf("====== 菜单 ======\n 1. 打印成绩 \n 0. 退出 \n 请输入：");
}

void print_scores(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        printf("%d\t", arr[i]);
    }
    printf("\n");
}

int main(void) {
    system("chcp 65001 > nul");
    int i;
    char word[] = "embedded";
    char first[20] = "Zhang";
    char last[] = "San";
    int count[10] = {11,321,34,124,414,141,212,1414,64,73} ;
    int size = 10;
    int choice;

    for(i = 0; word[i] != '\0'; i++) {
        printf("%c ", word[i]);
    }
    printf("\n");
    strcat(first, " ");
    strcat(first, last);
    printf("first: %s\n", first);
    printf("偶数个数为：%d\n",count_even(count, size));
    do{
        show_menu();
        scanf("%d", &choice);
        if(choice == 1) {
            print_scores(count, size);
        } else if(choice == 0) {
            printf("退出\n");
        } else {
            printf("无效输出\n");
        }
    } while(choice != 0);
    return 0;
}
