#include<stdio.h>
int main(){
	int input_num ;
	int num1 ;
	for (;;){
		printf("输入数字：\n");
		fflush(stdin);
		scanf("%d",&input_num);
		if (input_num == 999){
			break;
		}
		num1 += input_num;
	}
	printf("输入的数字之和：%d\n",num1 );
}
