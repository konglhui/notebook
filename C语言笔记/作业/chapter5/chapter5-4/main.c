#include<stdio.h>

int  main(){
	int ch;
	int num1 = 1;
	int num2 = 0;
	int num3 = 0;
	for (num1 = 1;num1<10;num1++){
		printf("��������\n");
		fflush(stdin);
		scanf("%d",&ch);
		if (ch<0){
			continue;
		}
		else if(ch>=0 && ch != 999){
			num2++;
			num3 += ch;
		}
		else{
			break;
		}

	}
	printf("����֮��Ϊ��%d",num3);

}
