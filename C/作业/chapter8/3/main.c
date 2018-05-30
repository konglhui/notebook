#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num[10] = {24,23,23,14,55,36,57,18,39,43};
    int *ptr_num = &num;
    int i,index_min,index_max;
    int min = 10000000;
    int max = 0;
    for (i = 0;i<10;i++)
    {
        if(*(ptr_num+i) < min)
        {
            min = *(ptr_num+i);
            index_min = i;
        }
        if(*(ptr_num+i) > max)
        {
            max = *(ptr_num+i);
            index_max = i;
        }
    }
    *(ptr_num+index_min) = *ptr_num;
    *ptr_num = min;
    *(ptr_num+index_max) = *(ptr_num + 9);
    *(ptr_num+9) = max;
    for (i = 0;i<10;i++)
    {
        printf("%d\n",*(ptr_num+i));
    }
    return 0;
}
