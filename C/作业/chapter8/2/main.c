#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 345;
    int j = 45467;
    int k = 54;
    int *pi = &i;
    int *pj = &j;
    int *pk = &k;
    if (*pi < *pj && *pi < *pk)
    {
        printf("%d\n",*pi);
        if (*pj<*pk)
        {
            printf("%d\n%d\n",*pj,*pk);
        }
        else
        {
            printf("%d\n,%d\n",*pk,*pj);
        }

    }
    else if(*pj < *pi && *pj < *pk)
    {
        printf("%d\n",*pj);
        if (*pi<*pk)
        {
            printf("%d\n%d\n",*pi,*pk);
        }
        else
        {
            printf("%d\n,%d\n",*pk,*pi);
        }

    }
    else
    {
        printf("%d\n",*pk);
        if (*pi<*pj)
        {
            printf("%d\n%d\n",*pi,*pj);
        }
        else
        {
            printf("%d\n,%d\n",*pj,*pi);
        }

    }
    return 0;
}
