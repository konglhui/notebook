#include <stdio.h>
#include <stdlib.h>

int main()
{
    char answer;
    int num1,num2;
    answer = 'y';

    while (answer == 'y'){
        printf("请输入一个数字：\n");
        scanf("%d",&num1);
        num2 = 0;
        while (num1>=num2){
            printf("%d\n",num2);
            num2++;
        }
        printf("你是否想继续：(y/n)\n");
        fflush(stdin);
        scanf("%c",&answer);
    }
    return 0;
}
