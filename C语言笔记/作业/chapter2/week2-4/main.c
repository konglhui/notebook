#include <stdio.h>
#include <stdlib.h>

void main()
{
    char chara,charb;
    printf("输入一个小写字母：\n");
    scanf("%c",&chara);
    charb = chara -32;
    printf("大写字母为：%c\n",charb);
    return 0;
}
