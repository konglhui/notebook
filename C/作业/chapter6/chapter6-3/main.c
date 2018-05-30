#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j,k;
    int temp = 0;
    int legal_num[10];
    for (j = 0;j<10;j++)
    {
        printf("请输入一个数字：");
        scanf("%d",&legal_num[j]);
    }
    for(i = 0;i<9;i++)
    {
        for (k=0;k<10-i-1;k++)
        {
            if (legal_num[k] >  legal_num[k+1])
            {
                temp = legal_num[k];
                legal_num[k] = legal_num[k+1];
                legal_num[k+1] = temp;
            }
        }
    }

    for (i = 0;i<10;i++){
        printf("%d\t",legal_num[i]);
    }

}
