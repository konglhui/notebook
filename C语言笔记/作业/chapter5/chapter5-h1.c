#include<stdio.h>

void main(){
	int const_num = 4;
	int sum= 0;
	int sum_single = 1;
	int i = 1;
	int j = 1;
	for (;i <= const_num;i++){
		for (;j <= i;j++){
			sum_single = j*sum_single;
		}
		sum +=sum_single;
	}
	printf("%d\n",sum );
}