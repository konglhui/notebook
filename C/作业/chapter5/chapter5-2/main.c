#include<stdio.h>
int main(){
	int input_num ;
	int num1 ;
	for (;;){
		printf("�������֣�\n");
		fflush(stdin);
		scanf("%d",&input_num);
		if (input_num == 999){
			break;
		}
		num1 += input_num;
	}
	printf("���������֮�ͣ�%d\n",num1 );
}
