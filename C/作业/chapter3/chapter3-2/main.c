#include <stdio.h>
#include <stdlib.h>

int main()
{
    char ch;
    float cost1;
    float cost2;
    float cost3;
    float total_cost;
    double discount;
    double pay;
    printf("�ǲ��ǻ�Ա����y/n��\n");
    scanf("%c",&ch);
    printf("�����һ����Ʒ�ķ��ã�\n");
    scanf("%f",&cost1);
    printf("����ڶ�����Ʒ�ķ��ã�\n");
    scanf("%f",&cost2);
    printf("�����������Ʒ�ķ��ã�\n");
    scanf("%f",&cost3);

    total_cost = cost1+cost2+cost3;
    if (ch == 'y' || total_cost >= 100){
        discount = total_cost*0.1;
    }
    if (ch == 'y' && total_cost >= 100){
        discount = total_cost*0.2;
    }
    pay = total_cost - discount;
    printf("�ܽ�� = %.2fԪ\n",total_cost);
    printf("�ۿ۽�� = %.2fԪ\n",discount);

    return 0;
}
