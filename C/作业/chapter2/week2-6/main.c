#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a ,b,c,d;
    c = 0;
    printf("输入你想输的两位整数：\n");
    scanf("%d",&a);
    b = a%10;
    d = a/10;
    c = c+b;
    b = d%10;
    c = c+b;
    printf("%d",c);
}
