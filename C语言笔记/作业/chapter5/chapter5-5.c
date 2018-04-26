#include<stdio.h>

int main(){
	int input_num;
	int linear_num;
	int row_num,row_num2;
	int i,j;
	printf("plz,input a number:\n");
	scanf("%d",&input_num);
	for (linear_num = 0;linear_num<(2*input_num+1);linear_num++){
		if (linear_num < input_num){
			row_num = input_num-linear_num;
			for (i = 0;i<row_num;i++){
				printf("%d",row_num);
			}
			printf("\n");
		}
		else if  (linear_num = input_num){
			printf("\n");
		}
		else if (linear_num > input_num){
			row_num2 = linear_num - input_num;
			for (j = 0;j < row_num2,j++){
				printf("%d",row_num2);
			
			}
			printf("\n");
		}
	}
}