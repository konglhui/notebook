#include<stdio.h>

int main()
{
	int num,i;
	int temp = 0;
	int array_num[8] = {0,0,0,0,0,0,0,0};
	printf("输入传输的密码：\n");
	scanf("%d",&num);
	for (i = 0;i<8;i++)
	{
		array_num[7-i] = (num%10 + 5)%10;
		num = num/10;
	}
	temp = array_num[0];
	array_num[0] = array_num[7];
	array_num[7] = temp;
	for (i = 0;i<7;i++)
	{
		printf("%d\t",array_num[i]);
	}

}