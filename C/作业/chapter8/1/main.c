#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 5;
    int j = 8;
    int *ptr_i = &i;
    int *ptr_j = &j;
    int temp;
    printf("%d,%d,%p,%p\n",i,j,&i,&j);
    temp = *ptr_i;
    *ptr_i = *ptr_j;
    *ptr_j = temp;

    printf("%d,%d,%p,%p\n",i,j,&i,&j);
}
