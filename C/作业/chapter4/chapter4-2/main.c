#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num1;
    int sum = 0;
    int number;
    printf("输入你想输入的值\n");
    scanf("%d",&num1);

    while (num1>0){
        number = num1%10;
        sum = sum+number;
        num1 = num1/10;
    }
    printf("sum:%d\n",sum);
    return 0;
}
