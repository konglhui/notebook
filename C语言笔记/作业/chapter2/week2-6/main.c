#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a ,b,c,d;
    c = 0;
    printf("�������������λ������\n");
    scanf("%d",&a);
    b = a%10;
    d = a/10;
    c = c+b;
    b = d%10;
    c = c+b;
    printf("%d",c);
}
