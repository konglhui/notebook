#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 14;
    int b = 5;
    int c = 8;
    int d;
    if (a > b){
        d = a;
        a = b;
        b = d;
    }
    if (a > c){
        d = a;
        a = c;
        c = d;
    }
    if (b > c){
        d = b;
        b = c;
        c = d;
    }
    printf("��С%d���м�%d�����%d",a,b,c);
    return 0;
}
