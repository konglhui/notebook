# include<stdio.h>

int main(){
	int i,j,k;
	printf("X |");
	for (i = 1;i <= 10;i++){
		printf("\t %d",i);
	}
	printf("\n");
	printf("---+");
	fflush(stdin);
	for(i = 0;i<=50;i++){
		printf("--");
	}
	printf("\n");
	for (j = 1;j<=10;j++){
		for (k = 0;k<=10;k++){
			if (k==0){
				printf("%d|", j);
			}
			else{
				printf("\t%d",j*k);
			}
		}
		printf("\n");
	}
}
