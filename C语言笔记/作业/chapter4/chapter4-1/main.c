#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int i = 0;
    int sum = 0;
    printf("��������ӵ���ֵ��\n");
    scanf("%d",&n);
    while(i<n){
        i++;
        sum = sum+i;
    }

    printf("%d\n",sum);
    return 0;
}
