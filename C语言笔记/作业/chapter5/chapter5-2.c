#include<stdio.h>

void main(){
	int breaknumber = 999;
	int input_num ;
	int num1 ;
	for (;;){
		printf("输入数字：\n");
		scanf("%c",&input_num);
		if (input_num == breaknumber){
			break;
		}
		num1 += input_num;
	}
	printf("输入的数字之和：%d\n",num1 );
}