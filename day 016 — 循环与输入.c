#include <stdio.h>

int main() {
    printf("=== Day 16: 循环与输入 ===\n\n");

    // 1. while 循环：打印 1 到 5
    printf("【while 循环】1 到 5:\n");
    int i = 1;
    while (i <= 5) {
        printf("%d ", i);
        i++;
    }
    printf("\n\n");

    // 2. for 循环：打印 1 到 5
    printf("【for 循环】1 到 5:\n");
    for (int j = 1; j <= 5; j++) {
        printf("%d ", j);
    }
    printf("\n\n");

    // 3. do-while 循环：至少执行一次
    printf("【do-while 循环】\n");
    int k = 1;
    do {
        printf("第 %d 次执行\n", k);
        k++;
    } while (k <= 3);
    printf("\n");

    // 4. scanf 交互：摄氏转华氏（用户输入）
    printf("【scanf 交互】摄氏转华氏\n");
    float input_c;
    printf("请输入摄氏温度: ");
    scanf("%f", &input_c);
    float output_f = input_c * 9.0f / 5.0f + 32.0f;
    printf("%.2f°C = %.2f°F\n\n", input_c, output_f);

    // 5. 交互式温度转换器（do-while 循环）
    printf("【交互式温度转换器】\n");
    int choice;
    float value, result;
    do {
        printf("\n===== 温度转换器 =====\n");
        printf("1. 摄氏 -> 华氏\n");
        printf("2. 华氏 -> 摄氏\n");
        printf("0. 退出\n");
        printf("请选择: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("请输入摄氏温度: ");
                scanf("%f", &value);
                result = value * 9.0f / 5.0f + 32.0f;
                printf("%.2f°C = %.2f°F\n", value, result);
                break;
            case 2:
                printf("请输入华氏温度: ");
                scanf("%f", &value);
                result = (value - 32.0f) * 5.0f / 9.0f;
                printf("%.2f°F = %.2f°C\n", value, result);
                break;
            case 0:
                printf("再见！\n");
                break;
            default:
                printf("无效选项，请重新选择。\n");
        }
    } while (choice != 0);

    return 0;
}
