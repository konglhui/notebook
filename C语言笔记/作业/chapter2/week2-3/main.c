#include <stdio.h>
#include <stdlib.h>

int main()
{
    int basic;
    int wujia;
    int fangzu;
    int gongzi;
    printf("����������ʣ�\n");
    scanf("%d", &basic);
    wujia = basic*40/100;
    fangzu = basic*20/100;
    gongzi = basic+wujia+fangzu;
    printf("��۽�����%d\n���������%d\nʵ�ʹ��ʣ�%d\n",wujia,fangzu,gongzi);
    return 0;
}
