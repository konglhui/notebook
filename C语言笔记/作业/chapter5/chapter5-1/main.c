#include<stdio.h>

int main(){
	char ch;
	int num1 = 1;
	int num2 = 0;
	int num3 = 0;
	for (num1=1;num1<10;num1 ++){
		printf("nihao\n");
		fflush(stdin);
		scanf("%c",&ch);
		if (ch>='a' && ch <= 'z'){
			num2 ++;
		}

	}
	num3 = 10 - num2;
	printf("��д��ĸ��%d����Сд��ĸ��%d��\n",num3,num2 );

}
