#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j;
    int num;
    int count = 0;
    int inlegal_count = 0;
    int legal_num[3] = {1,2,3};
    for (j = 0;j<10;j++)
    {
        printf("请输入一个数字：");
        scanf("%d",&num);
        for (i=0;i<3;i++)
        {
            if (num == legal_num[i])
            {
                break;
            }
        }
        if(i == 3)
        {
            count++;
        }
    }
    inlegal_count = 10-count;
    printf("非法数字个数是：%d,合法数字是：%d",count,inlegal_count);
}
