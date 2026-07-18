// if (条件1) {
//    条件1成立
// } else if (条件2) {
//    条件2成立
// } else {
//    所有条件都不成立
// }

//成绩等级
#include <stdio.h>
#include <stdlib.h>
int main() {
     system("chcp 65001 > nul");  // 添加这一行
    int score;

    printf("请输入成绩：");
    scanf("%d", &score);

    if (score < 0 || score > 100) {
        printf("成绩无效\n");
    } else if (score >= 90) {
        printf("成绩为A\n");
    } else if (score >= 80) {
        printf("成绩为B\n");
    } else if (score >= 70) {
        printf("成绩为C\n");
    } else if (score >= 60) {
        printf("成绩为D\n");
    } else {
        printf("成绩为E\n");
    }
    return 0;
}