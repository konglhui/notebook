#include <stdio.h>
#include <stdlib.h>

void main()
{
    double huashi,sheshi;
    printf("输入当前的华氏温度：\n");
    scanf("%lf",&huashi);
    sheshi = (huashi-32.0)*5/9.0;
    printf("转换后摄氏温度为：%.2f\n",sheshi);
}
