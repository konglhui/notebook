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
    printf("是不是会员？（y/n）\n");
    scanf("%c",&ch);
    printf("购买第一件商品的费用：\n");
    scanf("%f",&cost1);
    printf("购买第二件商品的费用：\n");
    scanf("%f",&cost2);
    printf("购买第三件商品的费用：\n");
    scanf("%f",&cost3);

    total_cost = cost1+cost2+cost3;
    if (ch == 'y' || total_cost >= 100){
        discount = total_cost*0.1;
    }
    if (ch == 'y' && total_cost >= 100){
        discount = total_cost*0.2;
    }
    pay = total_cost - discount;
    printf("总金额 = %.2f元\n",total_cost);
    printf("折扣金额 = %.2f元\n",discount);

    return 0;
}
