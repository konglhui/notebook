#include<stdio.h>

int main(){
	int i = 1;
	for (;i<=5;i++){
		if(i==1 || i ==  5){
			printf("  *\n");
		}
		else if (i == 2 || i == 4){
			printf(" * *\n");
		}
		else{
			printf("*   *\n");
		}
	}

}