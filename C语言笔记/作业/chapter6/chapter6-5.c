#include<stdio.h>

int main()
{
	int i;
	double avg=0;
	int sum=0;
	int legal_num[10] = {18,25,7,36,13,2,89,63,12,34};
	for (i = 0;i<10;i++)
    {
    	sum += legal_num[i];
	}
	avg = sum / 10;
	printf("平均值为：%.2f %d\n",avg,sum);
	for (i = 0;i<10;i++)
	{
		if (legal_num[i] > avg)
		{
			printf("%d\t",legal_num[i]);
		}
	}
}