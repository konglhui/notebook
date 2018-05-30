#include <stdio.h>
#include <stdlib.h>

int main()
{
    int basic;
    int wujia;
    int fangzu;
    int gongzi;
    printf("输入基本工资：\n");
    scanf("%d", &basic);
    wujia = basic*40/100;
    fangzu = basic*20/100;
    gongzi = basic+wujia+fangzu;
    printf("物价津贴：%d\n房租津贴：%d\n实际工资：%d\n",wujia,fangzu,gongzi);
    return 0;
}
