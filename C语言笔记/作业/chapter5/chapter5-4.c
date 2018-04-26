#include<stdio.h>

void main(){
	int ch;
	int num1 = 1;
	int num2 = 0;
	int num3 = 0;
	for (num1;num1<10;num1++){
		printf("输入数字：\n");
		scanf("%d",&ch);
		if (ch<0){
			continue;
		}
		else if(ch>=0 && ch != 999){
			num2++
			num3 += ch;
		}
		else{
			break;
		}

	}
	printf("大写字母有%d个，小写字母有%d个\n",num3,num2 );

}