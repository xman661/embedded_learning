#include <stdio.h>
#include <stdlib.h>

int main(void) {
int i;
int scores[5] = {90, 85, 100, 92, 88};
int steps[5];

steps[0] = 155;
steps[1] = 152;
steps[2] = 56;
steps[3] = 120;
steps[4] = 15;


    system("chcp 65001 > nul");
    for(i = 0; i < 5; i++) {
        printf("scores[%d] = %d, steps[%d] = %d\n", i, scores[i], i, steps[i]);
    }
    return 0;
}
