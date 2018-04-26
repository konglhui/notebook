#include<stdio.h>

void main(){
	char ch;
	int num1 = 1;
	int num2 = 0;
	int num3 = 0;
	for (num1;num1<10;num1++){
		printf("输入字符：\n");
		scanf("%c",&ch);
		if (ch>='a' && ch <= "z"){
			num2++;
		}

	}
	num3 = 10 - num2;
	printf("大写字母有%d个，小写字母有%d个\n",num3,num2 );



}