#include <stdio.h>
#include <stdlib.h>

int main()
{
    int count = 8;
    int index,i,temp;
    int credits[8] = {18,25,7,36,13,2,89,63};
    temp = credits[0];
    for (i = 0;i<count;i++)
    {
        if (temp <= credits[i])
        {
            index = i;
        }
    }
    printf("积分最大的索引为：%d\n",index);
}
